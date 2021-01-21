"""
Collections module - Counter

Collections -> High-performance Container DataTypes

Counter -> receive an iterable as parameter and create an object
of type collections.counter, which seems like a dictionary, and
contain the objects from the iterator as keys and the occurrence
numbers as values.
"""

# Using counter
from collections import Counter

new_list = [1, 2, 4, 12, 1, 2, 1, 2, 41, 2412, 5, 12,
            52141123, 12, 1, 25, 12, 31231, 5565, 756, 54,
            7854, 63, 54, 52, 452345, 2436, 5565, 41, 7854]

counter_type = Counter(new_list)
print(f"""The object counter_type is type {type(counter_type)} \
and the value is {counter_type}""", end="\n\n")


print("Counter is used with ANY ITERABLE!")
print(Counter("This is a Counter applied to a string."))
print(Counter({'a': 2, 'b': 3, 'c': 2}.values()))


long_string = """
In the past few decades, the field of quantum condensed matter physics has seen rapid
and, at times, almost revolutionary development. Undoubtedly, the success of the field
owes much to ground-breaking advances in experiment: already the controlled fabrication
of phase coherent electron devices on the nanoscale is commonplace (if not yet routine),
while the realization of ultra–cold atomic gases presents a new arena in which to explore
strong interaction and condensation phenomena in Fermi and Bose systems. These, along
with many other examples, have opened entirely new perspectives on the quantum physics
of many-particle systems. Yet, important as it is, experimental progress alone does not,
perhaps, fully explain the appeal of modern condensed matter physics. Indeed, in concert
with these experimental developments, there has been a “quiet revolution” in condensed
matter theory, which has seen phenomena in seemingly quite different systems united by
common physical mechanisms. This relentless “unification” of condensed matter theory,
which has drawn increasingly on the language of low-energy quantum field theory, betrays
the astonishing degree of universality, not fully appreciated in the early literature.
On a truly microscopic level, all forms of quantum matter can be formulated as a many-
body Hamiltonian encoding the fundamental interactions of the constituent particles. How-
ever, in contrast with many other areas of physics, in practically all cases of interest in
condensed matter the structure of this operator conveys as much information about the
properties of the system as, say, the knowledge of the basic chemical constituents tells us
about the behavior of a living organism! Rather, in the condensed matter environment,
it has been a long-standing tenet that the degrees of freedom relevant to the low-energy
properties of a system are very often not the microscopic. Although, in earlier times, the
passage between the microscopic degrees of freedom and the relevant low-energy degrees of
freedom has remained more or less transparent, in recent years this situation has changed
profoundly. It is a hallmark of many “deep” problems of modern condensed matter physics
that the connection between the two levels involves complex and, at times, even controversial
mappings. To understand why, it is helpful to place these ideas on a firmer footing.
Historically, the development of modern condensed matter physics has, to a large extent,
hinged on the “unreasonable” success and “notorious” failures of non-interacting theo-
ries. The apparent impotency of interactions observed in a wide range of physical sys-
tems can be attributed to a deep and far-reaching principle of adiabatic continuity: the
ixx
quantum numbers that characterize a many-body system are determined by fundamen-
tal symmetries (translation, rotation, particle exchange, etc.). Providing that the integrity
of the symmetries is maintained, the elementary “quasi-particle” excitations of an inter-
acting system can be usually traced back “adiabatically” to those of the bare particle
excitations present in the non-interacting system. Formally, one can say that the radius
of convergence of perturbation theory extends beyond the region in which the pertur-
bation is small. For example, this quasi-particle correspondence, embodied in Landau’s
Fermi-liquid theory, has provided a reliable platform for the investigation of the wide
range of Fermi systems from conventional metals to 3 helium fluids and cold atomic Fermi
gases.
However, being contingent on symmetry, the principle of adiabatic continuity and, with
it, the quasi-particle correspondence, must be abandoned at a phase transition. Here, inter-
actions typically effect a substantial rearrangement of the many-body ground state. In the
symmetry-broken phase, a system may – and frequently does – exhibit elementary exci-
tations very different from those of the parent non-interacting phase. These elementary
excitations may be classified as new species of quasi-particle with their own characteristic
quantum numbers, or they may represent a new kind of excitation – a collective mode –
engaging the cooperative motion of many bare particles. Many familiar examples fall into
this category: when ions or electrons condense from a liquid into a solid phase, translational
symmetry is broken and the elementary excitations – phonons – involve the motion of many
individual bare particles. Less mundane, at certain field strengths, the effective low-energy
degrees of freedom of a two-dimensional electron gas subject to a magnetic field (the quan-
tum Hall system) appear as quasi-particles carrying a rational fraction (!) of the elementary
electron charge – an effect manifestly non-perturbative in character.
This reorganization lends itself to a hierarchical perspective of condensed matter already
familiar in the realm of particle physics. Each phase of matter is associated with a unique
“non-interacting” reference state with its own characteristic quasi-particle excitations – a
product only of the fundamental symmetries that classify the phase. While one stays within
a given phase, one may draw on the principle of continuity to infer the influence of inter-
actions. Yet this hierarchical picture delivers two profound implications. Firstly, within the
quasi-particle framework, the underlying “bare” or elementary particles remain invisible
(witness the fractionally charged quasi-particle excitations of the fractional quantum Hall
fluid!). (To quote from P. W. Anderson’s now famous article “More is different,” (Science
177 (1972), 393–6), “the ability to reduce everything to simple fundamental laws does not
imply the ability to start from those laws and reconstruct the universe.”) Secondly, while
the capacity to conceive of new types of interaction is almost unbounded (arguably the
most attractive feature of the condensed matter environment!), the freedom to identify
non-interacting or free theories is strongly limited, constrained by the space of fundamen-
tal symmetries. When this is combined with the principle of continuity, the origin of the
observed “universality” in condensed matter is revealed. Although the principles of adia-
batic continuity, universality, and the importance of symmetries have been anticipated and
emphasized long ago by visionary theorists, it is perhaps not until relatively recently that
their mainstream consequences have become visible.xi
How can these concepts be embedded into a theoretical framework? At first sight, the
many-body problem seems overwhelmingly daunting. In a typical system, there exist some
10 23 particles interacting strongly with their neighbors. Monitoring the collective dynamics,
even in a classical system, is evidently a hopeless enterprise. Yet, from our discussion above,
it is clear that, by focussing on the coordinates of the collective degrees of freedom, one
may develop a manageable theory involving only a restricted set of excitations. The success
of quantum field theory in describing low-energy theories of particle physics as a successive
hierarchy of broken symmetries makes its application in the present context quite natural.
As well as presenting a convenient and efficient microscopic formulation of the many-body
problem, the quantum field theory description provides a vehicle to systematically identify,
isolate, and develop a low-energy theory of the collective field. Moreover, when cast as a field
integral, the quantum field theory affords a classification of interacting systems into a small
number of universality classes defined by their fundamental symmetries (a phenomenon not
confined by the boundaries of condensed matter – many concepts originally developed in
medium- or high-energy physics afford a seamless application in condensed matter). This
phenomenon has triggered a massive trend of unification in modern theoretical physics.
Indeed, by now, several sub-fields of theoretical physics have emerged (such as conformal
field theory, random matrix theory, etc.) that define themselves not so much through any
specific application as by a certain conceptual or methodological framework.
In deference to the importance attached to the subject, in recent years a number of
texts have been written on the subject of quantum field theory within condensed matter.
It is, therefore, pertinent for a reader to question the motivation for the present text.
Firstly, the principal role of this text is as a primer aimed at elevating graduate students
to a level where they can engage in independent research. Secondly, while the discussion
of conceptual aspects takes priority over the exposure to the gamut of condensed matter
applications, we have endeavored to keep the text firmly rooted in practical experimental
application. Thirdly, as well as routine exercises, the present text includes extended problems
which are designed to provide a bridge from formal manipulations to research-oriented
thinking. Indeed, in this context, readers may note that some of the “answered” problems
are deliberately designed to challenge: it is, after all, important to develop a certain degree
of intuitive understanding of formal structures and, sadly, this can be acquired only by
persistent and, at times, even frustrating training!
With this background, let us now discuss in more detail the organization of the text.
To prepare for the discussion of field theory and functional integral techniques we begin in
Chapter 1 by introducing the notion of a classical and a quantum field. Here we focus on
the problem of lattice vibrations in the discrete harmonic chain, and its “ancestor” in the
problem of classical and quantum electrodynamics. The development of field integral meth-
ods for the many-body system relies on the formulation of quantum mechanical theories in
the framework of the second quantization. In Chapter 2 we present a formal and detailed
introduction to the general methodology. To assimilate this technique, and motivate some
of the examples discussed later in the text, a number of separate and substantial appli-
cations are explored in this chapter. In the first of these, we present (in second-quantized
form) a somewhat cursory survey of the classification of metals and insulators, identifying axii
canonical set of model Hamiltonians, some of which form source material for later chapters.
In the case of the one-dimensional system, we will show how the spectrum of elementary
collective excitations can be inferred using purely operator methods within the framework
of the bosonization scheme. Finally, to close the chapter, we will discuss the application of
the second quantization to the low-energy dynamics of quantum mechanical spin systems.
As a final basic ingredient in the development of the quantum field theory, in Chapter 3 we
introduce the Feynman path integral for the single-particle system. As well as represent-
ing a prototype for higher-dimensional field theories, the path integral method provides a
valuable and recurring computational tool. This being so, we have included in this chapter
a pedagogical discussion of a number of rich and instructive applications which range from
the canonical example of a particle confined to a single or double quantum well, to the
tunneling of extended objects (quantum fields), quantum dissipation, and the path integral
formulation of spin.
Having accumulated all of the necessary background, in Chapter 4 we turn to the formula-
tion and development of the field integral of the quantum many-particle system. Beginning
with a discussion of coherent states for Fermi and Bose systems, we develop the many-
body path integral from first principles. Although the emphasis in the present text is on
the field integral formulation, the majority of early and seminal works in the many-body
literature were developed in the framework of diagrammatic perturbation theory. To make
contact with this important class of approximation schemes, in Chapter 5 we explore the
way diagrammatic perturbation series expansions can be developed systematically from the
field integral. Employing the φ 4 -theory as a canonical example, we describe how to explore
the properties of a system in a high order of perturbation theory around a known refer-
ence state. To cement these ideas, we apply these techniques to the problem of the weakly
interacting electron gas.
Although the field integral formulation provides a convenient means to organize pertur-
bative approximation schemes as a diagrammatic series expansion, its real power lies in
its ability to identify non-trivial reference ground states, or “mean-fields,” and to provide
a framework in which low-energy theories of collective excitations can be developed. In
Chapter 6, a fusion of perturbative and mean-field methods is used to develop analyti-
cal machinery powerful enough to address a spectrum of rich applications ranging from
metallic magnetism and superconductivity to superfluidity. To bridge the gap between the
(often abstract) formalism of the field integral, and the arena of practical application, it is
necessary to infer the behavior of correlation functions. Beginning with a brief survey of con-
cepts and techniques of experimental condensed matter physics, in Chapter 7 we highlight
the importance of correlation functions and explore their connection with the theoretical
formalism developed in previous chapters. In particular, we discuss how the response of
many-body systems to various types of electromagnetic perturbation can be described in
terms of correlation functions and how these functions can be computed by field theoretical
means.
Although the field integral is usually simple to formulate, its properties are not always
easy to uncover. Amongst the armory of tools available to the theorist, perhaps the
most adaptable and versatile is the method of the renormalization group. Motivatingxiii
our discussion with two introductory examples drawn from a classical and a quantum
theory, in Chapter 8 we become acquainted with the renormalization group method as a
concept whereby nonlinear theories can be analyzed beyond the level of plain perturbation
theory. With this background, we then proceed to discuss renormalization methods in more
rigorous and general terms, introducing the notion of scaling, dimensional analysis, and the
connection to the general theory of phase transitions and critical phenomena. To conclude
this chapter, we visit a number of concrete implementations of the renormalization group
scheme introduced and exemplified on a number of canonical applications.
In Chapter 9, we turn our attention to low-energy theories with non–trivial forms of
long-range order. Specifically, we will learn how to detect and classify topologically non-
trivial structures, and to understand their physical consequences. Specifically, we explore the
impact of topological terms (i.e. θ-terms, Wess–Zumino terms, and Chern–Simons terms)
on the behavior of low-energy field theories solely through the topology of the underlying
field configurations. Applications discussed in this chapter include persistent currents, ’t
Hooft’s θ-vacua, quantum spin chains, and the quantum Hall effects.
So far, our development of field theoretic methodologies has been tailored to the consid-
eration of single-particle quantum systems, or many-body systems in thermal equilibrium.
However, studies of classical nonequilibrium systems have a long and illustrious history,
dating back to the earliest studies of thermodynamics, and these days include a range of
applications from soft matter physics to population dynamics and ecology. At the same time,
the control afforded by modern mesoscopic semiconducting and metallic devices, quantum
optics, as well as ultracold atom physics now allow controlled access to quantum systems
driven far from equilibrium. For such systems, traditional quantum field theoretical method-
ologies are inappropriate.
Starting with the foundations of non-equilibrium statistical mechanics, from simple one-
step processes, to reaction–diffusion type systems, in Chapter 10 we begin by developing
Langevin and Fokker–Planck theory, from which we establish classical Boltzmann trans-
port equations. We then show how these techniques can be formulated in the language of
the functional integral developing the Doi–Peliti and Martin–Siggia–Rose techniques. We
conclude our discussion with applications to nonequilibrium phase transitions and driven
lattice gases. These studies of the classical nonequilibrium system provide a platform to
explore the quantum system. In Chapter 11, we develop the Keldysh approach to quantum
non-equilibrium systems based, again, on the functional integral technique. In particular,
we emphasize and exploit the close connections to classical nonequilibrium field theory, and
present applications to problems from the arena of quantum transport.
To focus and limit our discussion, we have endeavored to distill material considered
“essential” from the “merely interesting” or “background.” To formally acknowledge and
identify this classification, we have frequently included reference to material which we believe
may be of interest to the reader in placing the discussion in context, but which can be
skipped without losing the essential thread of the text. These intermissions are signaled in
the text as “Info” blocks.
At the end of each chapter, we have collected a number of pedagogical and instructive
problems. In some cases, the problems expand on some aspect of the main text requiring onlyxiv
an extension, or straightforward generalization, of a concept raised in the chapter. In other
cases, the problems rather complement the main text, visiting fresh applications of the same
qualitative material. Such problems take the form of case studies in which both the theory
and the setting chart new territory. The latter provide a vehicle to introduce some core areas
of physics not encountered in the main text, and allow the reader to assess the degree to
which the ideas in the chapter have been assimilated. With both types of questions to make
the problems more inclusive and useful as a reference, we have included (sometimes abridged,
and sometimes lengthy) answers. In this context, Section 6.5 assumes a somewhat special
role: the problem of phase coherent electron transport in weakly disordered media provides
a number of profoundly important problems of great theoretical and practical significance.
In preparing this section, it became apparent that the quantum disorder problem presents
an ideal environment in which many of the theoretical concepts introduced in the previous
chapters can be practiced and applied – to wit diagrammatic perturbation theory and series
expansions, mean-field theory and collective mode expansions, correlation functions and
linear response, and topology. We have therefore organized this material in the form of an
extended problem set in Chapter 6.
This concludes our introduction to the text. Throughout, we have tried to limit the range
of physical applications to examples which are rooted in experimental fact. We have resisted
the temptation to venture into more speculative areas of theoretical condensed matter at
the expense of excluding many modern and more-circumspect ideas which pervade the con-
densed matter literature. Moreover, since the applications are intended to help motivate and
support the field theoretical techniques, their discussion is, at times, necessarily superficial.
(For example, the hundreds pages of text in this volume could have been invested in their
entirety in the subject of superconductivity!) Therefore, where appropriate, we have tried
to direct interested readers to the more specialist literature.
In closing, we would like to express our gratitude to Jakob Müller-Hill, Tobias Micklitz,
Jan Müller, Natalja Strelkova, Franjo-Frankopan Velic, Andrea Wolff, and Markus Zowislok
for their invaluable assistance in the proofreading of the text. Moreover, we would also like
to thank Julia Meyer for her help in drafting problems. Finally we would like to acknowledge
Sasha Abanov for his advice and guidance in the drafting of the chapter on Topology.
As well as including additional material on the formulation of functional field integral
methods to classical and quantum nonequilibrium physics in Chapters 10 and 11, in prepar-
ing the second edition of the text, we have endeavored to remove some of the typographical
errors that crept into the first edition. Although it seems inevitable that some errors will
still have escaped identification, it is clear that many many more would have been missed
were it not for the vigilance of many friends and colleagues. In this context, we would partic-
ularly like to acknowledge the input of Piet Brouwer, Christoph Bruder, Chung-Pin Chou,
Jan von Delft, Karin Everschor, Andrej Fischer, Alex Gezerlis, Sven Gnutzmann, Colin
Kiegel, Tobias Lück, Patrick Neven, Achim Rosch, Max Schäfer, Matthias Sitte, Nobuhiko
Taniguchi, and Matthias Vojta.
"""


bunch_of_words = long_string.split()
bunch_of_words = Counter(bunch_of_words)
print(bunch_of_words.most_common(50))


print("\nSee the help for Counter:")
print(help(Counter), end="\n\n")

print("\nSee more methods from Counter:")
print(dir(Counter([])), end="\n\n")


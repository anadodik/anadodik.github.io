from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class Person:
    name: str
    picture_url: str
    email: str
    twitter: str
    website: str
    github: str
    linkedin: str
    google_scholar: str
    biography: str
    interests: list[str] | None = None
    address: str | None = None
    phone: str | None = None


@dataclass(kw_only=True, slots=True)
class Position:
    title: str
    description: str
    from_date: str
    to_date: str


@dataclass(kw_only=True, slots=True)
class Employment:
    company: str
    location: str
    periods: list[Position]


@dataclass(kw_only=True, slots=True)
class Education:
    institution: str
    degree: str
    location: str
    from_date: str
    to_date: str
    text: str


@dataclass(kw_only=True, slots=True)
class ResearchExperience:
    institution: str
    project: str
    location: str
    from_date: str
    to_date: str
    text: str


@dataclass(kw_only=True, slots=True)
class Publication:
    title: str
    nickname: str
    year: str
    authors: list[str]
    venue: str
    resources: dict[str, str]
    featured_image: str


@dataclass(kw_only=True, slots=True)
class Patent:
    name: str
    patent_number: str
    year: str
    authors: list[str]


@dataclass(kw_only=True, slots=True)
class Talk:
    name: str
    institution: str
    location: str
    date: str
    host: str


@dataclass(kw_only=True, slots=True)
class Teaching:
    pass


@dataclass(kw_only=True, slots=True)
class MediaAppearance:
    pass


@dataclass(kw_only=True, slots=True)
class Service:
    pass


BIOGRAPHY = """
Ana Dodik is a PhD student and Presidential Fellow at MIT CSAIL working on neural representations for geometry processing together with Justin Solomon and Vincent Sitzmann.

Prior to joining MIT, she spent two years developing next-generation virtual presence at Meta. She graduated with a Master's degree from ETH Zurich, where she spent a year collaborating with Disney Research Studios on problems at the intersection of machine learning and offline rendering.
"""

INTRO = """
Second-year PhD student at MIT <a href="https://www.eecs.mit.edu/">EECS</a>, <a href="https://www.csail.mit.edu/">CSAIL</a> advised by Prof. Justin Solomon and Prof. Vincent Sitzmann.
Working on problems at the intersection of graphics, vision, and algorithmic fairness.
</p><p>
Before MIT, I was a computer vision engineer at Meta. I have a Master's degree from ETH Zurich where I had the amazing opportunity to work with Disney Research Studios on path tracing research.
"""

INTERESTS = [
    "geometry processing",
    "machine learning",
    "neural representations",
    "Monte Carlo methods",
    "computer vision",
]

PERSON = Person(
    name="Ana Dodik",
    picture_url="photo.jpg",
    email="anadodik@mit.edu",
    twitter="https://twitter.com/ana_dodik",
    website="https://anadodik.github.io",
    github="https://github.com/anadodik",
    linkedin="https://www.linkedin.com/in/ana-dodik-246bb0150/",
    google_scholar="https://scholar.google.com/citations?user=cDmCKFcAAAAJ&sortby=pubdate",
    biography=BIOGRAPHY,
    interests=INTERESTS,
    address="",
    phone="",
)

PUBLICATIONS = [
    Publication(
        title="Variational Barycentric Coordinates",
        nickname="vbc",
        authors=["Ana Dodik", "Oded Stein", "Vincent Sitzmann", "Justin Solomon"],
        year="2023",
        venue="SIGGRAPH Asia (Journal Track)",
        resources={
            # "website": "#",
            "paper": "/publication/vbc/vbc.pdf",
            # "arXiv": "#",
            "supplementary": "/publication/vbc/supplemental.zip",
            # "talk": "#",
            "bibtex": "/publication/vbc/vbc.bib",
        },
        featured_image="featured.webp",
    ),
    Publication(
        title="Sex and Gender in the Computer Graphics Research Literature",
        nickname="gender-in-graphics",
        authors=[
            "Ana Dodik*",
            "Silvia Sellán*",
            "Theodore Kim",
            "Amanda Phillips",
            "(*joint first authors)",
        ],
        year="2022",
        venue="SIGGRAPH Talk",
        resources={
            "website": "https://gender-in-graphics.github.io/",
            "paper": "/publication/gender-in-graphics/gender-as-a-variable.pdf",
            "talk": "https://youtu.be/GOn3-P6KZ9E",
            "supplementary": "/publication/gender-in-graphics/gender-as-a-variable-supplement.pdf",
            "bibtex": "/publication/gender-in-graphics/dodiksellan2022gender.bib",
        },
        featured_image="featured.png",
    ),
    Publication(
        title="Path Guiding Using A Spatio-Directional Mixture Model",
        nickname="sdmm-paper",
        authors=["Ana Dodik", "Marios Papas", "Cengiz Öztireli", "Thomas Müller"],
        year="2021",
        venue="Computer Graphics Forum",
        resources={
            "paper": "publication/sdmm-paper/sdmm-paper.pdf",
            "thesis": "https://www.research-collection.ethz.ch/handle/20.500.11850/411118",
            "talk": "https://youtu.be/7D2r6K4rrqA?t=1774",
            "supplementary": "/publication/sdmm-paper/sdmm-paper-suppl.pdf",
            "video": "/publication/sdmm-paper/sdmm-video.mp4",
            "code": "https://github.com/anadodik/sdmm-mitsuba",
            "interactive": "/publication/sdmm-paper/website/index.html",
            "bibtex": "/publication/sdmm-paper/dodik21pathguiding.bib",
        },
        featured_image="featured.png",
    ),
]

OTHER_PUBLICATIONS = [
    # MSc
    # BSc
    # That CG conference about probabilistic connections.
]

EMPLOYMENT = [
    Employment(
        company="Meta",
        location="Zurich, Switzerland",
        periods=[
            Position(
                title="Computer Vision Engineer",
                description="Worked on 3D body reconstruction from images as part of the AR Commerce team. Co-supervised multiple research interns.",
                from_date="Sep 2020",
                to_date="May 2022",
            ),
            Position(
                title="Computer Vision Intern",
                description="Worked on grayscale image colorization using a hybrid machine-learning and optimization method. In collaboration with Facebook AI Research.",
                from_date="Jun 2019",
                to_date="Aug 2019",
            ),
        ],
    ),
    Employment(
        company="Microsoft",
        location="Belgrade, Serbia",
        periods=[
            Position(
                title="Computer Vision Intern",
                description="Researched and prototyped a novel method for a video editing effect as part of the Bend Reality project.",
                from_date="Jul 2017",
                to_date="Sep 2017",
            ),
        ],
    ),
]

PATENTS = [
    Patent(
        name="Automatic Colorization of Grayscale Stereo Images",
        patent_number="US-20240062425-A1",
        year="2022",
        authors=[
            "Catherine Marie Herold",
            "Alberto Garcia Garcia",
            "Romain Bachy",
            "Jan Oberländer",
            "Ana Dodik",
            "Ricardo da Silveira Cabral",
        ],
    ),
    Patent(
        name="Systems, methods, and media for colorizing grayscale images",
        patent_number="US-11451758-B1",
        year="2022",
        authors=[
            "Gaurav Chaurasia",
            "Alexander Sorkine Hornung",
            "David Novotny",
            "Ana Dodik",
        ],
    ),
]

EDUCATION = [
    Education(
        institution="Massachusetts Institute of Technology",
        degree="PhD Computer Science",
        location="Cambridge, MA, USA",
        from_date="Jul 2022",
        to_date="ongoing",
        text="Presidential fellow. Working on neural representations for geometry processing. Co-advised by Justin Solomon and Vincent Sitzmann.",
    ),
    Education(
        institution="ETH Zurich",
        degree="MSc Computer Science",
        location="Zurich, Switzerland",
        from_date="Sep 2017",
        to_date="Apr 2020",
        text="Focus on computer graphics, machine learning, and computer vision.",
    ),
    Education(
        institution="Vienna University of Technology",
        degree="BSc Software and Information Engineering",
        location="Vienna, Austria",
        from_date="Oct 2014",
        to_date="Jul 2017",
        text="German language preparation course in 2013/2014. GPA 1.50 (≈3.80 USA GPA).",
    ),
    Education(
        institution="United World College in Mostar",
        degree="International Baccalaureate Diploma",
        location="Mostar, Bosnia and Herzegovina",
        from_date="Sep 2011",
        to_date="May 2013",
        text="",
    ),
]


RESEARCH = [
    ResearchExperience(
        institution="Yale University",
        project="Research Consultant",
        location="New Haven, USA",
        from_date="Nov 2022",
        to_date="Feb 2022",
        text='"Worked with Prof. Theodore Kim on algorithmic fairness research."',
    ),
    ResearchExperience(
        institution="ETH Zurich, CGL, collaboration with Disney Research Studios and Nvidia Research.",
        project="Master's Thesis",
        location="Zurich, Switzerland",
        from_date="Sep 2018",
        to_date="May 2019",
        text='"Path Guiding using a Spatio-Directional Mixture Model"',
    ),
    ResearchExperience(
        institution="Disney Research Studios",
        project="Semester Project and Research Internship",
        location="Zurich, Switzerland",
        from_date="Jul 2018",
        to_date="Sep 2018",
        text="Researching strategies for guiding light paths and sampling BSDFs during rendering.",
    ),
    ResearchExperience(
        institution="ETH Zurich, CVG",
        project="Research assistant",
        location="Zurich, Switzerland",
        from_date="Nov 2017",
        to_date="Sep 2018",
        text="Applying machine learning to 3D geometry reconstruction from video.",
    ),
    ResearchExperience(
        institution="Vienna University of Technology, Rendering and Modeling Group",
        project="Bachelor's Thesis",
        location="Vienna, Austria",
        from_date="Jan 2017",
        to_date="Aug 2017",
        text='"Implementing Probabilistic Connections for Bidirectional Path Tracing in The Mitsuba Renderer."',
    ),
    ResearchExperience(
        institution="Vienna University of Technology, Rendering and Modeling Group",
        project="Undergraduate research assistant",
        location="Vienna, Austria",
        from_date="Jan 2016",
        to_date="Aug 2017",
        text="Literature review and work on a CUDA implementation for image-space filtering of Monte Carlo rendering noise.",
    ),
]

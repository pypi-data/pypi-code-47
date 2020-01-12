# Standard Library
from dataclasses import dataclass
from typing import Union, List

# Third party
import pandas as pd

# Local
from rewrite.problem import Problem
from rewrite import tex # For appending tex.NewPage to problemset

@dataclass(frozen=True)
class Assessment():
    """An assessment written in LaTeX with randomly generated parameters."""
    kind: str
    number: int
    fullpoints: Union[int, float]
    problems_path: object
    instructions: str = None
    hints: object = None
    problemset: tuple = None

    """
    THE DATES WILL BE OBTAINED FROM THE TERM AND COURSE OBJECTS WHEN THE ASSESSMENT IS GENERATED
    @property
    def period(self):
        return f"{self.start.strftime('%m/%d')} to {self.end.strftime('%m/%d')}"
    """

    @property
    def maxpoints(self):
        return sum(
            [sum(item.points) for item in self.problemset
             if isinstance(item, Problem)]
        )

    @classmethod
    def from_excel(cls, filename: str, names: List[str] = None) -> object:
        """Constructs a dictionary of assessments, keyed by the assessment.name, from an Excel workbook."""

        # Append '.xlsx' if necessary
        if isinstance(filename, str):
            if '.xlsx' not in filename:
                filename += '.xlsx'
        else:
            raise ValueError("The filename must be a string naming an Excel workbook.")

        # Load the data
        xls = pd.read_excel(filename, sheet_name=None)

        # Create the list of assessment names to create
        if names is None:
            names = list(assessments_df['name'])
        elif not isinstance(names, list):
            names = [names]
        # Filter out unwanted assessments
        df = xls['assessments']
        assessments_df = df[df.name.isin(names)]
        # Make a dictionary of assessments keyed by name
        assessments = {}
        for index, assessment_series in assessments_df.iterrows():
            name = assessment_series['name']
            problemset_df = xls[name]
            assessments[name] = Assessment.from_series(assessment_series, problemset_df)

        return assessments

    @classmethod
    def from_series(cls, series: object, problemset_df: object) -> object:
        """Constructs an assessment from a Pandas series and its problems from a Pandas dataframe."""

        # Load the instructions as a string
        filename = series['instructions']
        if pd.isna(filename):
            instructions = None
        else:
            with open(filename, 'r', encoding='utf-8') as file:
                instructions = file.read()

        # Load the formulas tex as a string
        filename = series['formulas']
        if pd.isna(filename):
            hints = None
        else:
            with open(filename, 'r', encoding='utf-8') as file:
                hints = file.read()

        # Create the problemset
        problems_path = series['problems_path']
        problemset = cls.problemset_from_df(problemset_df, problems_path)

        # Create the assessment
        assessment = cls(
            series['kind'],
            series['number'],
            series['fullpoints'],
            problems_path = problems_path,
            instructions=instructions,
            hints=hints,
            problemset=problemset,
        )

        return assessment

    @staticmethod
    def problemset_from_df(problemset_df: object, problems_path: str) -> object:
        """Constructs a problem set from a Pandas dataframe."""

        # Read the problemset data
        if problemset_df is None:
            problemset_df = pd.DataFrame(columns=['class', 'path', 'points', 'arguments'])
        # Create the problemset
        problemset = []
        for index, row in problemset_df.iterrows():
            class_name = row['class'].strip()
            if class_name == 'Problem':
                problem = Problem.from_series(row, problems_path)
                problemset.append(problem)
            elif class_name == 'NewPage':
                problemset.append(tex.NewPageMessage())
            else:
                raise NameError(f"{row['class']} is not a recognized class name")

        # Convert the problemset to an immutable type
        problemset = tuple(problemset)

        return problemset
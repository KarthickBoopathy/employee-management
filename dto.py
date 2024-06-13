from dataclasses import dataclass


@dataclass
class EmployeeDetailsDto:
    id: int
    first_name : str
    last_name : str
    email : str
    experience : int
    designation : str
from dataclasses import dataclass


@dataclass
class DbCreatorSettings:
    remote_configuration: bool
    default_admin: int | None = None
    disciplines_path: str = ''
    exel_data_path: str = ''

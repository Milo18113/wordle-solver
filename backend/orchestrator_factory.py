from backend.orchestrator import Orchestrator
from backend.solver import Solver
from backend.validator import Validator


class OrchestratorFactory:
    _instance: Orchestrator | None = None

    @classmethod
    def get_instance(cls) -> Orchestrator:
        if cls._instance is None:
            solver = Solver()
            validator = Validator()

            cls._instance = Orchestrator(solver, validator)

        return cls._instance
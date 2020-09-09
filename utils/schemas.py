from typing import List, Optional

from pydantic import BaseModel



class TestModel(BaseModel):
    parameter_set: int
    likelihood: float
    horizontal_flux_total: float
    vertical_flux: float
    PM1: float
    PM2_5: float
    PM10 : float
    #

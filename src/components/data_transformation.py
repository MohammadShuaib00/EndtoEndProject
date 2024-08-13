import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from src.logger.logging import logging
from src.exception.exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.utils.utils import save_object



@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
    
    


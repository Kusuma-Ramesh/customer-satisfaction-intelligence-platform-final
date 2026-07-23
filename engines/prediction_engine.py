# ===================================================
# IMPORTS
# ===================================================

import joblib
import pandas as pd

from pathlib import Path

from streamlit import dataframe

from config.mappings import (

    CLASS_MAPPING,
    RISK_MAPPING,
    SEGMENT_MAPPING

)


# ===================================================
# PROJECT DIRECTORY
# ===================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ===================================================
# MODEL PATHS
# ===================================================

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "customer_satisfaction_model_backup.pkl"

)


ENCODER_PATH = (

    BASE_DIR
    / "models"
    / "ordinal_encoder.pkl"

)


FEATURE_COLUMNS_PATH = (

    BASE_DIR
    / "models"
    / "feature_columns.pkl"

)


CATEGORICAL_COLUMNS_PATH = (

    BASE_DIR
    / "models"
    / "categorical_columns.pkl"

)


# ===================================================
# LOAD ML ASSETS
# ===================================================

def load_ml_assets():

    """
    Loads all ML assets.
    """

    try:

        model = joblib.load(

            MODEL_PATH

        )


        encoder = joblib.load(

            ENCODER_PATH

        )


        feature_columns = joblib.load(

            FEATURE_COLUMNS_PATH

        )


        categorical_columns = joblib.load(

            CATEGORICAL_COLUMNS_PATH

        )


        return {

            "status": "SUCCESS",

            "model": model,

            "encoder": encoder,

            "feature_columns":
            feature_columns,

            "categorical_columns":
            categorical_columns,

            "error": None

        }


    except Exception as error:


        return {

            "status": "FAILED",

            "model": None,

            "encoder": None,

            "feature_columns": None,

            "categorical_columns": None,

            "error": str(error)

        }

# ===================================================
# VALIDATE USER INPUTS
# ===================================================

def validate_inputs(user_inputs):

    """
    Validates user inputs before
    prediction.
    """

    try:

        required_features = [

    "channel_name",
    "category",
    "Sub-category",
    "Customer_City",
    "Product_category",
    "Item_price",
    "connected_handling_time",
    "Agent_name",
    "Tenure Bucket",
    "Agent Shift"

]

        # CHECK MISSING FEATURES

        for feature in required_features:

            if feature not in user_inputs:

                return {

                    "status": "FAILED",

                    "error":

                    f"{feature} is missing."

                }


        # CHECK ITEM PRICE

        if user_inputs["Item_price"] < 0:

            return {

                "status": "FAILED",

                "error":

                "Invalid Item Price."

            }


        # CHECK HANDLING TIME

        if user_inputs[
            "connected_handling_time"
        ] < 0:


            return {

                "status": "FAILED",

                "error":

                "Invalid Handling Time."

            }


        return {

            "status": "SUCCESS",

            "error": None

        }


    except Exception as error:


        return {

            "status": "FAILED",

            "error": str(error)

        }
    # ===================================================
# PREPROCESS INPUTS
# ===================================================

def preprocess_inputs(user_inputs):

    """
    Converts dictionary input
    into dataframe format.
    """

    try:

        dataframe = pd.DataFrame(
            [user_inputs]
        )

        return {

            "status": "SUCCESS",

            "dataframe": dataframe,

            "error": None

        }

    except Exception as error:

        return {

            "status": "FAILED",

            "dataframe": None,

            "error": str(error)

        }
    # ===================================================
# ENCODE INPUTS
# ===================================================

def encode_inputs(

        dataframe,
        encoder,
        categorical_columns

):

    try:

        dataframe[
            categorical_columns
        ] = encoder.transform(

            dataframe[
                categorical_columns
            ]

        )


        return {

            "status":"SUCCESS",

            "dataframe":dataframe,

            "error":None

        }


    except Exception as error:


        return{

            "status":"FAILED",

            "dataframe":None,

            "error":str(error)

        }
    # ===================================================
# MAKE PREDICTION
# ===================================================

def make_prediction(

        dataframe,
        model

):

    try:

        print("\nMODEL PREDICTION")
        print(model.predict(dataframe))

        prediction = model.predict(
            dataframe
        )[0]

        print("\nMODEL PROBABILITIES")
        print(model.predict_proba(dataframe))

        probabilities = (
            model.predict_proba(
                dataframe
            )[0]
        )

        return {

            "status":"SUCCESS",

            "prediction":prediction,

            "probabilities":probabilities,

            "error":None

        }

    except Exception as error:


        return{

            "status":"FAILED",

            "prediction":None,

            "probabilities":None,

            "error":str(error)

        }
    # ===================================================
# CONFIDENCE SCORE
# ===================================================

def calculate_confidence(probabilities):

    confidence = float(

        round(
            float(max(probabilities))*100,
            2
        )

    )

    return confidence

# ===================================================
# CLASS PROBABILITIES
# ===================================================

def get_class_probabilities(
        probabilities
):

    return {

        "Highly Unsatisfied":
        float(round(probabilities[0]*100,2)),

        "Unsatisfied":
        float(round(probabilities[1]*100,2)),

        "Neutral":
        float(round(probabilities[2]*100,2)),

        "Satisfied":
        float(round(probabilities[3]*100,2)),

        "Highly Satisfied":
        float(round(probabilities[4]*100,2))

    }
# ===================================================
# BUSINESS ANALYSIS
# ===================================================

def generate_business_analysis(
        prediction,
        confidence_score
):

    risk_level = RISK_MAPPING[
        prediction
    ]

    if prediction == 1:

        risk_level = "HIGH"

    elif prediction == 2:

        risk_level = "HIGH"

    elif prediction == 3:

        risk_level = "MEDIUM"

    elif prediction == 4:

        risk_level = "LOW"

    elif prediction == 5:

        risk_level = "LOW"

    if confidence_score < 40:

        risk_level = "HIGH"

    elif confidence_score < 60:

        if risk_level == "LOW":

            risk_level = "MEDIUM"

    return{

        "risk_level":
        risk_level,

        "customer_segment":

        SEGMENT_MAPPING[
            prediction
        ]

    }
# ===================================================
# RECOMMENDATIONS
# ===================================================

def generate_recommendations(
        prediction
):

    # Highly Unsatisfied
    if prediction == 1:

        return[
            "Immediate customer support is recommended.",
            "Prioritize customer retention efforts.",
            "Escalate the issue for urgent resolution."
        ]


    # Unsatisfied
    elif prediction == 2:

        return[
            "Improve service quality immediately.",
            "Review recent customer interactions.",
            "Provide personalized customer assistance."
        ]


    # Neutral
    elif prediction == 3:

        return[
            "Monitor customer experience closely.",
            "Collect customer feedback regularly.",
            "Improve response and resolution time."
        ]


    # Satisfied
    elif prediction == 4:

        return[
            "Maintain good service standards.",
            "Improve customer engagement.",
            "Provide proactive customer support."
        ]


    # Highly Satisfied
    else:

        return[
            "Maintain excellent service quality.",
            "Reward loyal customers with benefits.",
            "Encourage continued customer engagement."
        ]
    # ===================================================
# GENERATE RESULTS
# ===================================================

def generate_results(

        prediction,
        confidence_score,
        business_analysis,
        recommendations,
        class_probabilities

):

    return {

        "status": "SUCCESS",

        "prediction":

        CLASS_MAPPING[
            prediction
        ],


        "confidence_score":

        confidence_score,


        "risk_level":

        business_analysis[
            "risk_level"
        ],


        "customer_segment":

        business_analysis[
            "customer_segment"
        ],


        "recommendations":

        recommendations,


        "class_probabilities":

        class_probabilities,


        "error":

        None

    }
# ===================================================
# MAIN PREDICTION ENGINE
# ===================================================

def prediction_engine(user_inputs):


    # ------------------------
    # INPUT VALIDATION
    # ------------------------

    validation_results = (

        validate_inputs(
            user_inputs
        )

    )

    if validation_results["status"] == "FAILED":

        return validation_results


    # ------------------------
    # LOAD ML ASSETS
    # ------------------------

    assets = load_ml_assets()

    if assets["status"] == "FAILED":

        return assets


    # ------------------------
    # PREPROCESS INPUTS
    # ------------------------

    preprocessing_results = (

        preprocess_inputs(
            user_inputs
        )

    )

    if preprocessing_results["status"] == "FAILED":

        return preprocessing_results


    dataframe = (

        preprocessing_results[
            "dataframe"
        ]

    )


    # ------------------------
    # ENCODE INPUTS
    # ------------------------

    encoding_results = (

        encode_inputs(

            dataframe,

            assets["encoder"],

            assets[
                "categorical_columns"
            ]

        )

    )

    if encoding_results["status"] == "FAILED":

        return encoding_results


    dataframe = (

        encoding_results[
            "dataframe"
        ]

    )


     # ------------------------
    # FEATURE ALIGNMENT
    # ------------------------

    dataframe = dataframe[
        assets[
            "feature_columns"
        ]
    ]

    print("\nINPUT TO MODEL")
    print(dataframe)
    print("\n")


    # ------------------------
    # PREDICTION
    # ------------------------

    prediction_results = (
        make_prediction(
            dataframe,
            assets["model"]
        )
    )
    if prediction_results["status"] == "FAILED":
        return prediction_results
    prediction = (
        prediction_results[
            "prediction"
        ]
    )

    probabilities = (

        prediction_results[
            "probabilities"
        ]

    )


    # ------------------------
    # BUSINESS ANALYSIS
    # ------------------------

    confidence_score = calculate_confidence(
        probabilities
    )

    class_probabilities = (
        get_class_probabilities(
            probabilities
        )
    )

    business_analysis = (
        generate_business_analysis(
            prediction,
            confidence_score
        )
    )

    recommendations = (
        generate_recommendations(
            prediction
        )
    )

    # ------------------------
    # FINAL RESULTS
    # ------------------------

    results = (
        generate_results(
            prediction,
            confidence_score,
            business_analysis,
            recommendations,
            class_probabilities
        )
    )

    return results
from app.logging_utils import logger
from sqlalchemy import create_engine, text
import os, json

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(connection_string)


def get_submission(submission_id=None):
    logger.info(f"Fetching submission for SubmissionId: {submission_id}")
    with engine.connect() as conn:
        result = conn.execute(
            text("EXEC dbo.getQuestionierWithAnswers @submissionid=:submission_id"),
            {"submission_id": submission_id},
        ).mappings()
        row = result.fetchone()
        if row and row["prompt"]:
            submission = {
                "role": "user",
                "content": json.loads(json.dumps(row["prompt"])),
            }
            return submission
        else:
            logger.error(f"No prompt found for SubmissionId: {submission_id}")
            return []


def get_ingredients():
    logger.info(f"Fetching ingredients")
    with engine.connect() as conn:
        result = conn.execute(
            text("EXEC dbo.getIngrediant"),
        ).mappings()
        row = result.fetchone()
        if row and row["Ingrediants"]:
            ingredients = json.loads(row["Ingrediants"])
            # print(f"Ingredients: {ingredients}")
            for ingredient in ingredients:
                if isinstance(ingredient.get("IngrediantDataElement"), list):
                    ingredient["IngrediantDataElement"] = {
                        el["name"]: el["value"]
                        for el in ingredient["IngrediantDataElement"]
                    }

            return ingredients
        else:
            logger.error(f"No ingredients found")
            return []


if __name__ == "__main__":
    ingredients = get_ingredients()
    print(json.dumps(ingredients, indent=2))

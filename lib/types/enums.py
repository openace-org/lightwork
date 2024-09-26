from enum import Enum

class QuestionType(Enum):
    """
    Enum for question types
    """
    MULTIPLE_CHOICE = "multiple_choice"
    SHORT_TEXT_ANSWER = "short_answer"
    LONG_TEXT_ANSWER = "long_answer"
    FILL_IN_THE_BLANKS = "fill_in_the_blanks"
    TRUE_OR_FALSE = "true_or_false"
    MATCHING = "matching"
    SEQUENCING = "sequencing"
    NUMERIC_ANSWER = "numeric_answer"
    CODING = "coding"

class SessionType(Enum):
    """
    Enum for session types
    """
    SOLO = "solo"
    GROUP_STUDY = "group_study"

class OpenAIModel(Enum):
    """
    Enum for OpenAI models
    """
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_35_TURBO = "gpt-3.5-turbo"

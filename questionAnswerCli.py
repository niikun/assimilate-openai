#!/usr/bin/env python

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model and I also used AI via Github Copilot to write this command-line interface.
"""

import click
from oalib.solution import submit_question


@click.command()
@click.argument("text")
def main(text):
    """
    this is the main function that you ask the OpenAI API a question and get an answer.

    Example:
    ./questionAnswerCli.py "What is the capital of the United States?"
    """

    response = submit_question(text)
    print(response)

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
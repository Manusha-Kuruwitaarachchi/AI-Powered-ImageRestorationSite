Mad Libs Game
Overview

This project is a simple Mad Libs game that allows users to create a fun and customized story by replacing placeholders in a pre-defined text with their own words. The placeholders in the story are denoted by angle brackets (< and >).
Files

    story.txt: A text file containing the story with placeholders.
    mad_libs.py: The Python script that processes the story and interacts with the user.

How It Works

    Reading the Story:
        The script reads the story from the story.txt file.

    Extracting Placeholders:
        The script scans the story for placeholders marked by < and >.
        It identifies and collects all unique placeholders.

    Collecting User Input:
        For each unique placeholder, the script prompts the user to enter a word or phrase.
        The user's inputs are stored in a dictionary where keys are placeholders and values are the corresponding user inputs.

    Replacing Placeholders:
        The script replaces all placeholders in the story with the user-provided words.

    Displaying the Final Story:
        The script prints the final customized story with the user's inputs inserted.
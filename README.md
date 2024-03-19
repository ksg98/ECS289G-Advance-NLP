## Backend Project

This is a backend project using FastAPI to provide an API for chat prompts and Gemma API integration.

## FastAPI Documentation

FastAPI automatically generates interactive API documentation using Swagger UI. Once the server is running, you can access the documentation at `http://localhost:8001/docs`. This documentation allows you to test the API endpoints directly from the browser.

## Changing the Face Token

To change the face token used for authentication with the Gemma API, update the `HEADERS` variable in the `main.py` file:

```python
HEADERS = {"Authorization": "Bearer your_new_face_token_here"}
```
Replace your_new_face_token_here with your new face token.

## BERT Model
The BERT model used in this project is defined in the `bert.ipynb` notebook. After training, the final model is saved in the `final_bert_model` directory. Make sure to load this model in the `main.py` file for the application to function correctly.

# Installation

To set up the project, first clone the repository:

```bash

git clone https://your-repository-url.git
cd your-project-directory
```
Then, install the required dependencies:

```bash
pip install -r requirements.txt
```
#Running the Server
To start the FastAPI server, run the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```
The server will be available at http://localhost:5000.

# Prompt Dataset

`jailbreak_prompts.csv` and `regular_prompts.csv` is the collected prompts in our study. The meaning of each column is as follows.

| Column   | Description |
| -------- | ----------- |
| platform |  The platform of the prompt, i.e., Reddit.      |
| source   |  The source  of the prompt, i.e., r/ChatGPT.  |
| prompt   | The extracted prompt. |
| jailbreak | If it is True, then it is identified as a jailbreak prompt. |
| created_at   | Created time of the prompt. Obtained from the source. |
| date   | Date extracted from `created_at` value. |
| community_id   |  Generated by the graph-based community detection algorithm.        |
| community_name |  Community name referred in our paper.        |



# Forbidden Question Set

The complete forbidden question set is `forbidden_question_set.csv.zip`.

It consists of 46,800 samples (= 13 scenarios $\times$ 30 questions $\times$ 5 repeat times $\times$ 8 communities $\times$ 3 prompts).

 The meaning of each column is as follows.

| Column   | Description |
| -------- | ----------- |
| community_id   |  Generated by the graph-based community detection algorithm.        |
| community_name |  Community name referred in our paper.        |
| prompt_type |  The type of prompt, i.e., earlist, latest, or the most closeness one in the community.     |
| prompt   | The extracted prompt. |
| content_policy_id | Content policy id. |
| content_policy_name   | The content policy name, i.e., illegal activity. |
| q_id | Question id. |
| question | The question. |
| response_idx | For each question, we ask it five times.  |
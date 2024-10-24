# WordPress Author Style Imitator

A tool that analyzes an author's writing style from their WordPress.com blog posts and helps generate new content that mimics their unique voice.

## Project Structure

- `src/`: Contains the source code for the project
  - `auth/`: Authentication related code.
  - `notebooks/`: Jupyter notebooks for the main pipeline
  - `utils/`: Utility functions and helpers
- `data/`: Contains the processed data (not included in repo)
  - `author_posts/`: Raw posts by author
  - `classified_posts/`: Posts after confidentiality classification
  - `author_instructions/`: Generated writing style instructions
  - `post_instructions/`: Style-applied drafts

## Setup

1. Clone this repository
2. Create a `.env` file in the root directory with:
   - `WPCOM_CLIENT_SECRET`: WordPress.com API client secret
   - `WPCOM_ACCESS_TOKEN`: WordPress.com API access token
   - `ANTHROPIC_API_KEY`: Anthropic API key for Claude
3. Install required packages using Poetry: `poetry install`

## Notebooks

1. Obtain WordPress.com API credentials and set up an app (see [WordPress.com API documentation](https://developer.wordpress.com/docs/))
2. Get an Anthropic API key for Claude 3.5
3. Run `auth_get_token.py` to obtain an access token
4. Execute notebooks in the following order:
  - `retrieve_posts.ipynb`
  - `llm_classify_posts.ipynb`
  - `llm_generate_author_prompts.ipynb`
  - `llm_apply_author_style.ipynb`

### retrieve_posts.ipynb
Fetches blog posts and engagement metrics from WordPress.com API. The notebook:
- Retrieves posts using WordPress.com REST API
- Collects metadata (views, likes, comments)
- Handles rate limiting and pagination
- Saves posts organized by domain and author
- Processes cross-posts between different WordPress.com sites

### llm_classify_posts.ipynb
Uses a local LLM to identify and filter out posts containing confidential information. The notebook:
- Processes the top 50 posts by engagement score
- Uses Ollama with Qwen 2.5 model for classification
- Identifies sensitive/confidential content
- Saves classification results with reasoning
- Filters out confidential posts from further processing

### llm_generate_author_prompts.ipynb
Analyzes non-confidential posts to generate comprehensive writing style instructions. The notebook:
- Takes filtered posts from previous step
- Uses Claude 3.5 to analyze writing patterns
- Generates detailed style instructions covering:
  - Tone and voice
  - Content structure
  - Language patterns
  - Technical depth
  - Engagement techniques
- Saves instructions for use in content generation

### llm_apply_author_style.ipynb
Applies the generated style instructions to new content. The notebook:
- Takes a draft post as input
- Uses style instructions and example posts
- Leverages Claude 3.5 to rewrite content
- Maintains technical accuracy while matching author's voice
- Saves the style-applied output

## Note on Data Privacy

This repository intentionally excludes input and output data as the development used internal blog posts from Automattic. When using this tool, ensure you have appropriate permissions for the blog posts you analyze.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

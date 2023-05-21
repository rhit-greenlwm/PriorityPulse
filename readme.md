# Priority Pulse

Priority Pulse is an application that allows you to process .eml files and perform two NLP tasks on them: priority sorting and sentiment analysis. It leverages NLP techniques, including a Hugging Face transformer model, to provide valuable insights from your email data.

## Features

1. Priority Sorting: The application analyzes the content of multiple .eml files and assigns an urgency score to each email based on its content. It then sorts the emails based on this score, helping you identify and address the most critical messages first.

2. Sentiment Analysis: Priority Pulse uses a Hugging Face transformer model to perform sentiment analysis on the text within the .eml files. It provides sentiment labels (e.g., positive, negative, or neutral) for each email, giving you an overview of the overall sentiment within your email conversations.

## Requirements

- Python 3.x
- Dependencies listed in the `requirements.txt` file

## Installation

1. Clone the repository:

```git clone https://github.com/your-username/prioritypulse.git```

2. Navigate to the project directory:

```cd prioritypulse```

3. Install the required dependencies using pip:

```pip install -r requirements.txt```

## Usage

1. Place your .eml files in the `emails` directory.

2. Run the application:

```python main.py```

3. The application will process the .eml files, perform priority sorting, and display the sorted emails along with their urgency scores and sentiment analysis results.

## Configuration

You can modify the behavior of Priority Pulse by editing the configuration file `config.ini`. The available options include:

- `threshold`: The urgency score threshold for determining high-priority emails.
- `sentiment_model`: The name of the Hugging Face transformer model to use for sentiment analysis.

## Contributing

Contributions are welcome! If you'd like to contribute to Priority Pulse, please follow these steps:

1. Fork the repository.

2. Create a new branch:

```git checkout -b feature/your-feature```

3. Make your changes and commit them:

```git commit -m "Add your commit message"```

4. Push your changes to your forked repository:

```git push origin feature/your-feature```

5. Open a pull request on the original repository, describing your changes and their purpose.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to reach out to the project maintainer at [greenlwm@rose-hulman.edu](mailto:greenlwm@rose-hulman.edu).

Enjoy using Priority Pulse!

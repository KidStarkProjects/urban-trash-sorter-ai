# Smart Urban Trash Sorter AI

  <h3>AI-Powered Waste Management for Smarter Cities</h3>
</div>

---

### Project Overview

**Smart Urban Trash Sorter AI** is an innovative solution designed to streamline waste management in urban environments. This application leverages a pre-trained image classification model from Hugging Face to instantly identify different types of waste, providing users with actionable recycling or disposal instructions.

The project addresses the critical challenge of waste segregation, promoting sustainable urban living by making recycling intuitive and accessible to everyone.

---

### Technical Implementation

- **Core Technology:** The application is built on **Python**, using the **Hugging Face `transformers`** library to interface with the `google/vit-base-patch16-224` Vision Transformer model.
- **Frontend:** A simple yet effective user interface is created with **Gradio**, allowing for rapid prototyping and deployment.
- **Functionality:** The system classifies images and maps the model's output to a predefined set of waste categories (e.g., plastics, paper, organics), providing a clear and specific recommendation for each item.

---

### How to Run

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/KidStarkProjects/urban-trash-sorter-ai.git](https://github.com/KidStarkProjects/urban-trash-sorter-ai.git)
    cd urban-trash-sorter-ai
    ```
2.  **Install Dependencies:**
    ```bash
    pip install transformers torch gradio
    ```
3.  **Launch the Application:**
    ```bash
    python app.py
    ```
    The application will launch on a local server and provide a public URL for sharing.

---

### File Structure

-   `app.py`: Contains all the necessary code, including model loading, inference logic, and the Gradio interface setup.
-   `README.md`: Project documentation.

---

### Contribution

This project was developed by **Samuel Simanjuntak** for the **AIC** competition. For inquiries, please contact samuel.simanjuntak990@gmail.com .

---

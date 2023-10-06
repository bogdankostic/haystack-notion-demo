FROM python:3.10-slim

# Copy ui package
COPY . /ui

# Install custom ui package and streamlit dependency
RUN pip install --upgrade pip && \
    pip install streamlit && \
    pip install /ui/

WORKDIR /ui
EXPOSE 8501

# cmd for running the API
CMD ["python", "-m", "streamlit", "run", "webapp.py"]

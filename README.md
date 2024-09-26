# Lightwork

Lightwork is a tool powered by OpenAI LLMs designed to trivialise the process of conducting productive study sessions. 

## Goals

Lightwork aims to:

- **Effortlessly maximize knowledge intake.** Lightwork incentivizes students to learn with a *3-Think* framework: (1) think first principle, (2) think actively, and (3) think repeatedly. Furthermore, generated materials are ordered in a way that optimizes rate of absorption.

- **Induce dopamine and motivate.** You get memes, ice creams (the digital currency for OpenYan Market), and more rewards for every bit of progression. You can also invite others, such as your friends, to consume generated materials together in a healthy competitive setting!

## Serving lightwork locally

Lightwork resources are exposed via a FastAPI Web API server, which can be ran by executing:

```bash
uvicorn main:app --port 7001
```

**Using Docker -** You can alternatively build a docker image and run the app in a container:

```bash
# Build the image
docker build -t openyan-lightwork:latest .

# Serve the container
docker run -p 7001:7001 -d --name openyan-lightwork openyan-lightwork:latest
```

API v1 should be accessible at `localhost:7001/v1`
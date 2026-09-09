# Handwriting Recognizer — pure static site (runs anywhere)

A fully self-contained, **serverless** web demo: you draw a digit on a canvas and a
neural network predicts it **100% inside your browser**. No Python, no backend, no
database — deployable to GitHub Pages (or any static host) and it keeps working forever.

## Pages

- **`index.html`** — the handwriting demo. Inference = `softmax(ReLU(xW₁+b₁)W₂+b₂)`
  computed in JavaScript with weights from a **scikit-learn `MLPClassifier`** trained on MNIST.
- **`presentation.html`** — a self-contained model presentation:
  1. What model is used
  2. Structure of the model (784 → 256 ReLU → 10 softmax, 203,530 parameters)
  3. Train / validation loss curves (real per-epoch values, recorded from an actual run)
  4. The code that creates and trains the model
- **`model_weights.json`** — exported float32 weights (1 MB, base64) + layer layout.

## How it works

1. Training happened once: `MLPClassifier` (256 hidden units, ReLU, Adam, early stopping)
   reached **98% test accuracy** on MNIST. See the local project
   `D:\deep learning\handwriting-demo\backend\train_sklearn.py`.
2. `export_weights.py` dumped the weights to `model_weights.json` (verified to reproduce
   scikit-learn's predictions exactly).
3. `index.html` decodes the weights, downscales the canvas to 28×28, and runs the same
   forward pass in JS — nothing ever leaves your device.

## Deploy to GitHub Pages (one-time, ~3 minutes)

1. Create an empty repository on https://github.com/new (e.g. name it `handwriting-demo`, keep it public).
2. From this folder, run:

   ```powershell
   git init
   git add .
   git commit -m "Handwriting recognizer: static demo + presentation"
   git branch -M main
   git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
   git push -u origin main
   ```

3. In the repo on GitHub: **Settings → Pages → Source: Deploy from a branch → Branch: `main` / `/ (root)` → Save**.
4. Done. Everyone can open:

   ```
   https://<YOUR_USERNAME>.github.io/<REPO_NAME>/              (demo)
   https://<YOUR_USERNAME>.github.io/<REPO_NAME>/presentation.html
   ```

## Try locally without deploying

```powershell
python -m http.server 8080        # from this folder
# open http://127.0.0.1:8080
```

## Model summary

| item            | value                                              |
|-----------------|----------------------------------------------------|
| model           | `MLPClassifier` (scikit-learn)                     |
| architecture    | 784 → 256 (ReLU) → 10 (softmax)                    |
| parameters      | 203,530                                            |
| loss            | cross-entropy (Adam, L2 α=1e-4, batch 256)         |
| training data   | MNIST train (60,000 digits, white-on-black 28×28)  |
| test accuracy   | ~98%                                               |
| inference       | in-browser JavaScript, ~1–2 ms per digit           |

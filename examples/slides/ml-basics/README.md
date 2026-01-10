# Basic Machine Learning Presentation

A comprehensive introduction to machine learning concepts with Mermaid diagrams.

## Contents

**17 slides** covering fundamental ML concepts:
- Introduction to Machine Learning
- Types of ML (Supervised, Unsupervised, Reinforcement)
- ML Workflow
- Features & Labels
- Training & Testing
- Common Algorithms
- Evaluation Metrics
- Model Evaluation Process
- Overfitting vs Underfitting
- Feature Engineering
- Neural Networks
- Deep Learning
- Best Practices
- Common Pitfalls
- Next Steps

## Diagrams

Four Mermaid diagrams created and converted to SVG:

1. **ml-types.svg** - Hierarchical view of ML types and algorithms
2. **ml-workflow.svg** - Complete ML pipeline with feedback loops
3. **neural-network.svg** - Neural network architecture with layers
4. **model-evaluation.svg** - Model evaluation and improvement process

## Building

### HTML Output
```bash
marp slides.md -o slides.html
```

### PDF Output
```bash
marp slides.md -o slides.pdf
```

### Watch Mode (for development)
```bash
marp -w slides.md
```

## Viewing

Open `slides.html` in any modern web browser, or use Marp for VS Code for live preview.

## Theme

- **Style**: Dark (invert class)
- **Background**: #1E1E1E
- **Text**: #D4D4D4
- **Layout**: Clean, technical aesthetic

## Regenerating Diagrams

If you need to regenerate the SVG diagrams from source:

```bash
cd diagrams
mmdc -i ml-types.mmd -o ml-types.svg -b transparent
mmdc -i ml-workflow.mmd -o ml-workflow.svg -b transparent
mmdc -i neural-network.mmd -o neural-network.svg -b transparent
mmdc -i model-evaluation.mmd -o model-evaluation.svg -b transparent
```

Or use the batch script:
```bash
cd diagrams
for f in *.mmd; do mmdc -i "$f" -o "${f%.mmd}.svg" -b transparent; done
```

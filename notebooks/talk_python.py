import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Talk Python**
    ___
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## [Building Data Science with Foundation LLM Models](https://talkpython.fm/episodes/show/526/building-data-science-with-foundation-llm-models)
    ###Evaluating Agents
    - Find modes of failure
     - Retrieval
     - Tool calls
     - Resolved tickets
    - Write tests with good coverage
    - Gather labelled examples
    """)
    return


@app.cell
def _(mo):
    s = mo.ui.slider(1, 5)
    s
    return (s,)


@app.cell
def _(mo, s):
    mo.md(rf"""
    {"##" + "🍃"*s.value}
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

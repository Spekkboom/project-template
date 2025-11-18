import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    mo.md("# **Marimo Notebook Template**")
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Imports
    """)
    return


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    import altair as alt
    return pl, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Config
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    config = mo.ui.dictionary(
        {
            "text": mo.ui.text(),
            "slider": mo.ui.slider(start=1, stop=10),
            "date": mo.ui.date(),
        }
    )
    config
    return (config,)


@app.cell
def _(config):
    config.value["slider"]
    return


@app.cell
def _(mo):
    mo.md(r"""
    ###
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Analysis**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    slider = mo.ui.slider(1, 10)
    slider
    return (slider,)


@app.cell
def _(pl, slider):
    df = pl.DataFrame({
        "x": ["a", "b", "c"],
        "y": [1, 2, slider.value],
        "z": ["example1", "another", "wow"]
    })
    return (df,)


@app.cell(hide_code=True)
def _(df, px):
    px.bar(df, x = "x", y = "y")
    return


@app.cell
def _(df, mo):
    category = mo.ui.dropdown(df.select("x").to_series().to_list())
    category
    return


@app.cell
def _(df):
    # df.filter(pl.col("x") == category.value)
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ___
    """)
    return


if __name__ == "__main__":
    app.run()

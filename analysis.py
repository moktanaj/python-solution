import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# data = pd.read_csv("Data/data/sandbox-installs.csv")

# Creating country_app_used_count dataframe to check which country is using the app most.


def country_app_used_count(data):

    country_app_used_count_df = data.groupby('geo_country')['geo_country'].count().to_frame(name='count')\
        .sort_values(by="count", ascending=False).reset_index()

    return country_app_used_count_df

# plotting the country_app_used_count dataframe using matplotlib


def plot_country_app_used_count(data):
    country_df = country_app_used_count(data)
    plt.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(25, 10))
    plt.bar(country_df['geo_country'], country_df['count'], color='orange')
    plt.title("Number of times App used in Various Countries")
    plt.xlabel("Countries")
    plt.ylabel("App Count")
    fig.autofmt_xdate()
    plt.show()

# Creating Dataframe of Country using different versions and count.


def country_app_version_used_count(data):
    app_ver_df = data.groupby(['app_version', 'geo_country'])['app_version'].count()\
        .to_frame(name='count').reset_index()
    return app_ver_df

# Plotting Different versions of app used in Different countries


def plot_country_app_version_used_count(data):
    app_ver_ge20_df = country_app_version_used_count(data)
    sns.catplot(x="geo_country", y="count", hue="app_version", kind="bar", data=app_ver_ge20_df, height=5, aspect=2.5)
    plt.xticks(rotation=45)
    plt.title("Number of versions of App used in Various Countries")
    plt.xlabel("Countries using Different versions of App")
    plt.show()

# Creating a Dataframe of sources of App downloaded.


def app_downloaded_src(data):
    app_downloaded_src_df = pd.DataFrame(data.groupby('sku').size().to_frame(name="count").reset_index())
    return app_downloaded_src_df

# plotting the Sources and its count from where the app has been downloaded.


def plot_app_downloaded_src(data):
    app_downloaded_src_df = app_downloaded_src(data)
    plt.style.use('fivethirtyeight')
    plt.figure(figsize=(8, 3))
    plt.bar(app_downloaded_src_df['sku'], app_downloaded_src_df['count'], color='green')
    plt.title("Number of App Downloaded from different sources")
    plt.xlabel("Download Sources")
    plt.ylabel("Number of App downloaded")
    plt.show()

# Creating data frame to count the sources of App installed.


def app_installed_sources(data):

    """ Data cleaning is required in the install_source column
    as some of the rows contain digit as an installed sources.
    In my opinion, Those are error in data. Hence, those rows are removed."""

    app_installed_sources_df = data.groupby('install_source').size().to_frame(name='count').reset_index()
    # some of the sources are digit so we need to get rid of it by converting it into NaN.
    app_installed_sources_df['install_source'] = app_installed_sources_df['install_source']\
        .mask(pd.to_numeric(app_installed_sources_df['install_source'], errors='coerce').notna())
    # All the NaN rows are dropped from installed_source column.
    app_installed_sources_df = app_installed_sources_df.dropna()
    return app_installed_sources_df.reset_index(drop=True)

# plotting the Different Sources from where App has been installed.


def plot_app_installed_sources(data):
    app_installed_sources_df = app_installed_sources(data)
    plt.style.use('fivethirtyeight')
    plt.figure(figsize=(20, 10))
    plt.plot(app_installed_sources_df['install_source'], app_installed_sources_df['count'], color='orange')
    plt.title("App installed 3 and more times from different sources")
    plt.xlabel("installed Sources")
    plt.ylabel("Number of times installed")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
# Main Function


def main_analysis(filename):
    try:
        data = pd.read_csv(filename)
        plot_country_app_used_count(data)
        plot_country_app_version_used_count(data)
        plot_app_downloaded_src(data)
        plot_app_installed_sources(data)
    except Exception as e:
        return print("Analysic module failed" + e.str())
    return "Analysis module done"


if __name__ == "__main__":
    main_analysis()



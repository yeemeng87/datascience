{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center>\n",
    "    <img src=\"https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png\" width=\"300\" alt=\"cognitiveclass.ai logo\"  />\n",
    "</center>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **SpaceX  Falcon 9 First Stage Landing Prediction**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Assignment: Exploring and Preparing Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Estimated time needed: **70** minutes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this assignment, we will predict if the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is due to the fact that SpaceX can reuse the first stage.\n",
    "\n",
    "In this lab, you will perform Exploratory Data Analysis and Feature Engineering.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Falcon 9 first stage will land successfully\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing\\_1.gif)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Several examples of an unsuccessful landing are shown here:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most unsuccessful landings are planned. Space X performs a controlled landing in the oceans.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objectives\n",
    "\n",
    "Perform exploratory Data Analysis and Feature Engineering using `Pandas` and `Matplotlib`\n",
    "\n",
    "*   Exploratory Data Analysis\n",
    "*   Preparing Data  Feature Engineering\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Import Libraries and Define Auxiliary Functions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We will import the following libraries the lab\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# andas is a software library written for the Python programming language for data manipulation and analysis.\n",
    "import pandas as pd\n",
    "#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays\n",
    "import numpy as np\n",
    "# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.\n",
    "import matplotlib.pyplot as plt\n",
    "#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exploratory Data Analysis\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First, let's read the SpaceX dataset into a Pandas dataframe and print its summary\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>Date</th>\n",
       "      <th>BoosterVersion</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Orbit</th>\n",
       "      <th>LaunchSite</th>\n",
       "      <th>Outcome</th>\n",
       "      <th>Flights</th>\n",
       "      <th>GridFins</th>\n",
       "      <th>Reused</th>\n",
       "      <th>Legs</th>\n",
       "      <th>LandingPad</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Serial</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2010-06-04</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>6104.959412</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0003</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2012-05-22</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>525.000000</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0005</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2013-03-01</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>677.000000</td>\n",
       "      <td>ISS</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0007</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2013-09-29</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>PO</td>\n",
       "      <td>VAFB SLC 4E</td>\n",
       "      <td>False Ocean</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1003</td>\n",
       "      <td>-120.610829</td>\n",
       "      <td>34.632093</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2013-12-03</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>3170.000000</td>\n",
       "      <td>GTO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1004</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   FlightNumber        Date BoosterVersion  PayloadMass Orbit    LaunchSite  \\\n",
       "0             1  2010-06-04       Falcon 9  6104.959412   LEO  CCAFS SLC 40   \n",
       "1             2  2012-05-22       Falcon 9   525.000000   LEO  CCAFS SLC 40   \n",
       "2             3  2013-03-01       Falcon 9   677.000000   ISS  CCAFS SLC 40   \n",
       "3             4  2013-09-29       Falcon 9   500.000000    PO   VAFB SLC 4E   \n",
       "4             5  2013-12-03       Falcon 9  3170.000000   GTO  CCAFS SLC 40   \n",
       "\n",
       "       Outcome  Flights  GridFins  Reused   Legs LandingPad  Block  \\\n",
       "0    None None        1     False   False  False        NaN    1.0   \n",
       "1    None None        1     False   False  False        NaN    1.0   \n",
       "2    None None        1     False   False  False        NaN    1.0   \n",
       "3  False Ocean        1     False   False  False        NaN    1.0   \n",
       "4    None None        1     False   False  False        NaN    1.0   \n",
       "\n",
       "   ReusedCount Serial   Longitude   Latitude  Class  \n",
       "0            0  B0003  -80.577366  28.561857      0  \n",
       "1            0  B0005  -80.577366  28.561857      0  \n",
       "2            0  B0007  -80.577366  28.561857      0  \n",
       "3            0  B1003 -120.610829  34.632093      0  \n",
       "4            0  B1004  -80.577366  28.561857      0  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv\")\n",
    "\n",
    "# If you were unable to complete the previous lab correctly you can uncomment and load this csv\n",
    "\n",
    "# df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')\n",
    "\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Orbit\n",
       "GTO      27\n",
       "ISS      21\n",
       "VLEO     14\n",
       "PO        9\n",
       "LEO       7\n",
       "SSO       5\n",
       "MEO       3\n",
       "ES-L1     1\n",
       "GEO       1\n",
       "HEO       1\n",
       "SO        1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['Orbit']].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First, let's try to see how the `FlightNumber` (indicating the continuous launch attempts.) and `Payload` variables would affect the launch outcome.\n",
    "\n",
    "We can plot out the <code>FlightNumber</code> vs. <code>PayloadMass</code>and overlay the outcome of the launch. We see that as the flight number increases, the first stage is more likely to land successfully. The payload mass is also important; it seems the more massive the payload, the less likely the first stage will return.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1842.38x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(y=\"PayloadMass\", x=\"FlightNumber\", hue=\"Class\", data=df, aspect = 5)\n",
    "plt.xlabel(\"Flight Number\",fontsize=20)\n",
    "plt.ylabel(\"Pay load Mass (kg)\",fontsize=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that different launch sites have different success rates.  <code>CCAFS LC-40</code>, has a success rate of 60 %, while  <code>KSC LC-39A</code> and <code>VAFB SLC 4E</code> has a success rate of 77%.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, let's drill down to each site visualize its detailed launch records.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK 1: Visualize the relationship between Flight Number and Launch Site\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the function <code>catplot</code> to plot <code>FlightNumber</code> vs <code>LaunchSite</code>, set the  parameter <code>x</code>  parameter to <code>FlightNumber</code>,set the  <code>y</code> to <code>Launch Site</code> and set the parameter <code>hue</code> to <code>'class'</code>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1302.38x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a scatter point chart with x axis to be Flight Number and y axis to be the launch site, and hue to be the class value\n",
    "sns.catplot(y=\"LaunchSite\", x=\"FlightNumber\", hue=\"Class\", data=df, aspect = 3.5)\n",
    "plt.xlabel(\"Flight Number\",fontsize=20)\n",
    "plt.ylabel(\"Launch Site\",fontsize=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now try to explain the patterns you found in the Flight Number vs. Launch Site scatter point plots.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK 2: Visualize the relationship between Payload and Launch Site\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We also want to observe if there is any relationship between launch sites and their payload mass.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1302.38x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value\n",
    "sns.catplot(y=\"LaunchSite\", x=\"PayloadMass\", hue=\"Class\", data=df, aspect = 3.5)\n",
    "plt.xlabel(\"Pay load Mass (kg)\",fontsize=20)\n",
    "plt.ylabel(\"Launch Site\",fontsize=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now if you observe Payload Vs. Launch Site scatter point chart you will find for the VAFB-SLC  launchsite there are no  rockets  launched for  heavypayload mass(greater than 10000).\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK  3: Visualize the relationship between success rate of each orbit type\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we want to visually check if there are any relationship between success rate and orbit type.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a `bar chart` for the sucess rate of each orbit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfEAAAE9CAYAAAAbGFuyAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAaGElEQVR4nO3de5hkdX3n8feHQQRUJJGJIjPIiIjBCARGvAQN3kHJoqIr6MYH1AdRMFFXVza7GxIT4wUVo6LIE5F1o+B6iSAZRR8v6HpZLgYRCMgAAiOugkYUbwh8949zxhQ1famZ6dPdv57363nq6Tq/c6r609VV9elz6vQ5qSokSVJ7tlroAJIkadNY4pIkNcoSlySpUZa4JEmNssQlSWqUJS5JUqO2XugAG2unnXaq3XbbbaFjSJI0by6++OJbqmr5+HhzJb7bbrtx0UUXLXQMSZLmTZLrpxp3c7okSY2yxCVJapQlLklSoyxxSZIaZYlLktQoS1ySpEZZ4pIkNWqwEk9yepIfJrlsmvlJ8s4ka5NcmmS/obJIkrQUDbkmfgZw8AzzDwH26C/HAO8dMIskSUvOYCVeVV8GfjzDIocBH6zON4Adk+w8VB5JkpaahfxMfBfgxpHpdf2YJEmawEIeOz1TjNWUCybH0G1yZ9ddd73bvJvf+49zHmxjLX/Zf5px/jXvOmyekkxt91ecvaDffy6c/OGnLej3f9Xzz1vQ7y8tFVe+5wcLHYGHvfz+Cx1hzizkmvg6YOXI9ArgpqkWrKrTqmp1Va1evnyDk7hIkrRFWsgSPwd4Yb+X+qOBW6vq+wuYR5Kkpgy2OT3JmcBBwE5J1gEnAvcAqKpTgTXA04G1wC+Ao4fKIknSUjRYiVfVkbPML+C4ob6/JElLnUdskySpUZa4JEmNssQlSWqUJS5JUqMscUmSGmWJS5LUKEtckqRGWeKSJDXKEpckqVGWuCRJjbLEJUlqlCUuSVKjLHFJkhpliUuS1ChLXJKkRlnikiQ1yhKXJKlRlrgkSY2yxCVJapQlLklSoyxxSZIaZYlLktQoS1ySpEZZ4pIkNcoSlySpUZa4JEmNssQlSWqUJS5JUqMscUmSGmWJS5LUKEtckqRGWeKSJDVq64UOIEnSYvKDd1yw0BG4/ysPmGg518QlSWqUJS5JUqMscUmSGmWJS5LUKEtckqRGWeKSJDXKEpckqVGWuCRJjbLEJUlqlCUuSVKjBi3xJAcnuSrJ2iQnTDH/vkk+leRbSS5PcvSQeSRJWkoGK/Eky4BTgEOAvYAjk+w1tthxwBVVtQ9wEPC2JNsMlUmSpKVkyDXxA4C1VXVtVd0OnAUcNrZMAfdJEuDewI+BOwbMJEnSkjFkie8C3Dgyva4fG/Vu4PeBm4BvA39eVXcNmEmSpCVjyBLPFGM1Nv004BLggcC+wLuT7LDBHSXHJLkoyUU333zzXOeUJKlJQ5b4OmDlyPQKujXuUUcDn6jOWuA64GHjd1RVp1XV6qpavXz58sECS5LUkiFL/EJgjySr+p3VjgDOGVvmBuBJAEnuD+wJXDtgJkmSloyth7rjqrojyfHAecAy4PSqujzJsf38U4G/Ac5I8m26ze+vq6pbhsokSdJSMliJA1TVGmDN2NipI9dvAp46ZAZJkpYqj9gmSVKjLHFJkhpliUuS1ChLXJKkRlnikiQ1yhKXJKlRlrgkSY2yxCVJapQlLklSoyxxSZIaZYlLktQoS1ySpEZZ4pIkNcoSlySpUZa4JEmNssQlSWqUJS5JUqO2XugAkubHMz7+voWOwD8f/tKFjiAtKa6JS5LUKEtckqRGWeKSJDXKEpckqVGWuCRJjbLEJUlqlCUuSVKjLHFJkhpliUuS1ChLXJKkRlnikiQ1ymOnS1o0/sPHzl7Q73/Ocw6bcf5zP37ZPCWZ3kcP/4OFjqBFxDVxSZIaZYlLktQoS1ySpEZZ4pIkNcoSlySpUZa4JEmNmrjEk9xryCCSJGnjzFriSR6b5ArgX/vpfZK8Z/BkkiRpRpOsiZ8MPA34EUBVfQt4/JChJEnS7CbanF5VN44N3TlAFkmStBEmOezqjUkeC1SSbYA/o9+0LkmSFs4ka+LHAscBuwDrgH2Blw+YSZIkTWCSNfE9q+oFowNJ/gj46jCRpDYdcvaxC/r9P33YqQv6/SXNv0nWxN814dgGkhyc5Koka5OcMM0yByW5JMnlSc6f5H4lSdIMa+JJHgM8Flie5NUjs3YAls12x0mWAacAT6HbDH9hknOq6oqRZXYE3gMcXFU3JPm9TfopJEnaAs20Jr4NcG+6or/PyOWnwHMmuO8DgLVVdW1V3Q6cBYyfrPf5wCeq6gaAqvrhxsWXJGnLNe2aeFWdD5yf5Iyqun4T7nsXYPRf09YBjxpb5qHAPZJ8ie4PhL+vqg+O31GSY4BjAHbddddNiCJJ0tIzyY5tv0hyEvBwYNv1g1X1xFlulynGaorvvz/wJGA74OtJvlFV37nbjapOA04DWL169fh9SJK0RZpkx7YPAVcCq4C/Br4LXDjB7dYBK0emVwA3TbHMZ6rq51V1C/BlYJ8J7luSpC3eJCV+v6p6P/Cbqjq/ql4EPHqC210I7JFkVX+QmCOAc8aWORt4XJKtk2xPt7ndA8lIkjSBSTan/6b/+v0kz6Bbm14x242q6o4kxwPn0e3NfnpVXZ7k2H7+qVX1r0k+A1wK3AX8Q1Vdtik/iCRJW5pJSvxvk9wX+M90/x++A/DKSe68qtYAa8bGTh2bPgk4aZL7kyRJ/27WEq+qc/urtwJPgN8esU2SJC2gmQ72sgz4j3T/KvaZqrosyaHAX9DtSf6H8xNRkiRNZaY18ffT7V1+AfDOJNcDjwFOqKpPzkM2SZI0g5lKfDWwd1XdlWRb4BbgIVX1/+YnmiRJmslM/2J2e1XdBVBVvwK+Y4FLkrR4zLQm/rAkl/bXA+zeTweoqtp78HSSJGlaM5X4789bCkmStNFmOgHKppz0RJIkzZNJDrsqSZIWIUtckqRGbVSJJ/mdJO7QJknSIjBriSf5UpIdkvwu8C3gA0nePnw0SZI0k0nWxO9bVT8Fng18oKr2B548bCxJkjSbSUp86yQ70x1H/dzZFpYkSfNjkhJ/Pd05wddW1YVJHgxcPWwsSZI0m0lORfpR4KMj09cChw8ZSpIkzW7WEk/yFuBvgV8CnwH2AV5ZVf84cDbNk3NPP2ShI3Doiz690BEkqTmTbE5/ar9j26HAOuChwGsHTSVJkmY1SYnfo//6dODMqvrxgHkkSdKEZt2cDnwqyZV0m9NfnmQ58KthY0mSpNnMuiZeVScAjwFWV9VvgF8Ahw0dTJIkzWySI7ZtDxwHvLcfeiCweshQkiRpdpN8Jv4B4Hbgsf30Orq91SVJ0gKapMR3r6q3AL8BqKpfAhk0lSRJmtUkJX57ku2AAkiyO/DrQVNJkqRZTbJ3+ol0B3lZmeRDwB8BRw0ZSpIkzW6Sw65+Lsk3gUfTbUb/86q6ZfBkkiRpRpPsnf4s4I6q+ueqOhe4I8kzB08mSZJmNMln4idW1a3rJ6rqJ3Sb2CVJ0gKapMSnWmaSz9IlSdKAJinxi5K8PcnuSR6c5GTg4qGDSZKkmU1S4q+gO9jLR+jOK/4ruiO4SZKkBTTJ3uk/B06YhyySJGkjzFriSb5If6CXUVX1xEESSZKkiUyyg9prRq5vCxwO3DFMHEmSNKlJNqeP78T21STnD5RHkiRNaJLN6b87MrkVsD/wgMESSZKkiUyyOf1ius/EQ7cZ/TrgxUOGkiRJs5tkc/qq+QgiSZI2zrT/J57kkUkeMDL9wiRnJ3nn2CZ2SZK0AGY62Mv76A7yQpLHA28CPgjcCpw2fDRJkjSTmTanL6uqH/fXnwecVlUfBz6e5JLBk0mSpBnNtCa+LMn6kn8S8IWReROdACXJwUmuSrI2ybRHfes33d+Z5DmT3K8kSZq5jM8Ezk9yC/BL4CsASR5Ct0l9RkmWAacATwHWARcmOaeqrphiuTcD523STyBJ0hZq2hKvqjck+TywM/DZqlp/6NWt6E6KMpsDgLVVdS1AkrOAw4ArxpZ7BfBx4JEbmV2SpC3ajJvFq+obU4x9Z8L73gW4cWR6HfCo0QWS7AI8C3gilrgkSRtlklORbqpMMTZ+IpV3AK+rqjtnvKPkmCQXJbno5ptvnqt8kiQ1baId1DbROmDlyPQK4KaxZVYDZyUB2Al4epI7quqTowtV1Wn0/9a2evXqDc6oJknSlmjIEr8Q2CPJKuB7wBHA80cXGD0aXJIzgHPHC1ySJE1tsBKvqjuSHE+31/ky4PSqujzJsf38U4f63pIkbQmGXBOnqtYAa8bGpizvqjpqyCySJC01Q+7YJkmSBmSJS5LUKEtckqRGWeKSJDXKEpckqVGWuCRJjbLEJUlqlCUuSVKjLHFJkhpliUuS1ChLXJKkRlnikiQ1yhKXJKlRlrgkSY2yxCVJapQlLklSoyxxSZIaZYlLktQoS1ySpEZZ4pIkNcoSlySpUZa4JEmNssQlSWqUJS5JUqMscUmSGmWJS5LUKEtckqRGWeKSJDXKEpckqVGWuCRJjbLEJUlqlCUuSVKjLHFJkhpliUuS1ChLXJKkRlnikiQ1yhKXJKlRlrgkSY2yxCVJapQlLklSoyxxSZIaZYlLktQoS1ySpEYNWuJJDk5yVZK1SU6YYv4LklzaX76WZJ8h80iStJQMVuJJlgGnAIcAewFHJtlrbLHrgD+uqr2BvwFOGyqPJElLzZBr4gcAa6vq2qq6HTgLOGx0gar6WlX9Wz/5DWDFgHkkSVpShizxXYAbR6bX9WPTeTHw6QHzSJK0pGw94H1nirGacsHkCXQlfuA0848BjgHYdddd5yqfJElNG3JNfB2wcmR6BXDT+EJJ9gb+ATisqn401R1V1WlVtbqqVi9fvnyQsJIktWbIEr8Q2CPJqiTbAEcA54wukGRX4BPAn1bVdwbMIknSkjPY5vSquiPJ8cB5wDLg9Kq6PMmx/fxTgb8E7ge8JwnAHVW1eqhMkiQtJUN+Jk5VrQHWjI2dOnL9JcBLhswgSdJS5RHbJElqlCUuSVKjLHFJkhpliUuS1ChLXJKkRlnikiQ1yhKXJKlRlrgkSY2yxCVJapQlLklSoyxxSZIaZYlLktQoS1ySpEZZ4pIkNcoSlySpUZa4JEmNssQlSWqUJS5JUqMscUmSGmWJS5LUKEtckqRGWeKSJDXKEpckqVGWuCRJjbLEJUlqlCUuSVKjLHFJkhpliUuS1ChLXJKkRlnikiQ1yhKXJKlRlrgkSY2yxCVJapQlLklSoyxxSZIaZYlLktQoS1ySpEZZ4pIkNcoSlySpUZa4JEmNssQlSWqUJS5JUqMscUmSGjVoiSc5OMlVSdYmOWGK+Unyzn7+pUn2GzKPJElLyWAlnmQZcApwCLAXcGSSvcYWOwTYo78cA7x3qDySJC01Q66JHwCsraprq+p24CzgsLFlDgM+WJ1vADsm2XnATJIkLRlDlvguwI0j0+v6sY1dRpIkTWHrAe87U4zVJixDkmPoNrcD3Jbkqs3MNmon4JbNuoeX/+ncJJne5mX8s6ke5jm3eRlfPHjGzcr36hcs/scwvG8Oo0xps18r4dg5ijKtzXwM58Viz7j574nD27yMx81dkGls/mP4qg1GHjTVYkOW+Dpg5cj0CuCmTViGqjoNOG2uAwIkuaiqVg9x33PFjJtvseeDxZ9xsecDM86FxZ4PFn/G+cw35Ob0C4E9kqxKsg1wBHDO2DLnAC/s91J/NHBrVX1/wEySJC0Zg62JV9UdSY4HzgOWAadX1eVJju3nnwqsAZ4OrAV+ARw9VB5JkpaaITenU1Vr6Ip6dOzUkevFfHw6MbNBNtPPMTNuvsWeDxZ/xsWeD8w4FxZ7Plj8GectX7oelSRJrfGwq5IkNWpJlXiSO5NcMnI5oR8/NMm/JPlWkiuSvHSa2383yU5jYw9L8vUkv07ymgEy3z/Jh5Ncm+Ti/ns9K8lBSW4d+3me3N9mRZKzk1yd5Jokf9/vPDiIaTJe3me6IskvRzI+p99R8b/3+b6T5ItJHj5QttvGpo9K8u7++l8l+d7YY7hjP+/AJBckubK/HDPF3Q+WN8lW/SGHL0vy7SQXJlnVz3tRP3ZpP3/8IEmDZhsbWxSPYZJK8r9GprdOcnOSc/vpo/rp0Zx79fMenuQL/XPx6iT/I8ng/6k18n50WZKPJtm+H5/X1+8sGf9b/1q+tM/6qCTbJHlHn+3qPuuKBc407Xt4kmNGnoMXJDlwjvN8KcnTxsZemWRNksumWP6MJNeNPA+/NjLvmf3PdWX/Gn/mZgesqiVzAW6bYuwedP+2tqKfview5zS3/y6w09jY7wGPBN4AvGaO8wb4OnDsyNiDgFcABwHnTnObC4Cj++llwPuBkwZ6TKfN2F/fDbhs7DbH0+0LsX0//VTgGmDboX/nwFHAu/vrfzXV7wx4AHADsF8/vRNwMfCM+XqOAkcCHwO26qdXAL/Tf70GuG8/fm9g1dC5pnosF9NjCNwG/AuwXT99CHDJ+tfI6O997Hbb9Y/nU/vp7YFPA8fN5+MJfAh49Xy/fmfJ95j+tX3Pkd/hA4G39pmW9eNH95mzQJkexDTv4cCh/fNup356v/55+YA5zPRS4ANjY98AHsfYe18/7wzgOVOM70O3E/eqfnpVP7335uRbUmvi07gP3Q58PwKoql9X1cQHi6mqH1bVhcBvBsj2ROD2uvvOftdX1btmuc2vquoD/fJ30h0W4EXr/9JfBBlfR1fyv+iX/yzwNeAFA+TbFMcBZ1TVNwGq6hbgvwAbnKRnQDsD36+qu/oM66rq3+j+aPwZXWlRVbdV1XXzmGtSC/EYfhp4Rn/9SODMCW7zfOCr/XOQ/jl5PPP7uwb4CvAQ5v/1O5OdgVuq6td9lluAn9CV9qv6bPRZf91nX4hMP2P69/DXAa/tl6N/Pv5P5naH6Y8Bhya5J0CS3ej+2Fm3kffzGuDv1r+e+69vBF67OeGWWolvN7Y57XlV9WO6/0e/PsmZSV6QZLH83A8HvjnD/MeN/Ty797e5eHShqvop3V+fD1mAjHeTZAfgXlV1zdisi/r7mmt3+50Drx+b/6qR+V/sxzZ4DAfMN53/DfxJn+ttSf6wH/8W8APguiQfSPIn85hpOovlMTwLOCLJtsDewP8dm/+8sdfLdlPl7J+b9+6fq4NLsjXdloNvT5NnyNfvTD4LrOw/ZnhPkj/uM9zQZxo1X6+PDTLN8h4++POwqn5EtyXi4H7oCOAjTHF00REnjTwPPzRk1kH/xWwB/LKq9h0frKqXJHkE8GS6v4aeQrf5bVFJcgpwIHA73V9nX6mqQ8eWCVM/eaYbHyxjVT1yY27KMPnu9jtPchQweqSkk6vqrRNmmbd/1aiqdUn2pFu7eSLw+STPrarPJzmY7iOcJwEnJ9m/qv5qvrJNYVE8hlV1ab8WdCRj/7ra+0hVHT86MMPrhRnG58p2/R+W0K2Jvx942TTfd15ev6Oq6rYk+9NtFn4CXTG9cZoc85JvqkxJTtjI9/Ahsp5JV95n919fNMvyr62qj02Qa7OzLpY10sFV1ber6mS6X/7hSZaN/KU0vvY2Xy6n+wxnfcbj6N64l89ym7sdzq9fo1hJ99nfgmbs/4L/eZIHj83aD7higHybYoPHENifec7Xbxb8dFW9Fvg74Jn9eFXVBVX1Rro3jMPnM9eEFuoxPIfuM9tJNqXD1K+XB9N9Xv2zOc427pdVtW9/eUV1Z3Oc79fvjKrqzqr6UlWdSPcxw6HAg5LcZ2zReXv9TpHp8H78bu/h/eJX0D3vhs76SeBJSfaj2y9j4q2TI6Z6zWx21iVf4knuneSgkaF9gev7J8r6F9hfLkg4+AKwbZKXjYzN9rnY54Htk7wQfnve9rfRfT75i0WS8STgnf3mTNLtVX8g8OEB8m2KU4CjkuwLkOR+wJuBt8xXgCT7JXlgf30rus3D1yd5YP9Gsd6+wPXzlWsjLNRjeDrw+qr69oTLfwg4MP/+nx3bAe9kHn/XY+b79TutJHsm2WNkaF/gKrrPlN/eZ6PPuj3de8FCZPrBVO/h/fW3AG/un3/0z8ejgPfMZa6qug34Et3zb9I/IMe9Ffiv/dak9Z+t/wXd73+zwi2ZC3An3R6r6y9votuxbQ3dk/MS4KvA6mlu/126vSDX9Ze30+2Fuw74Kd1OH+uAHeYw8850n/VdR/e5yxeB59HtnX7r2M/znP42K4FPAVfT/fX+Lvq9OQd6XKfM2M/bjQ33Tg9wIt2el1cB5wOPGCjbbHunf2/sMdytn/d4uuP7X9lnfNk8PUfX751+MN3nY5f1l9OBben2xP1Cn+sS4HPA7vOU7a6R5/46ur2pF8VjOP577scO4u57p988lvOx/bxH0L0BX9U/J09kfva03iBzPz6vr98Z8u1Pt8PpFcClwCfo9ga/Z5/pmj7jp4CVC5hpJTO8h9N9RHFV/zy8EHj8QNmeRbfp+2H99G50OzyPvmaeS7d3+nVjz8Vt+ts8m27fiCv7r8/e3FwesU2SpEYt+c3pkiQtVZa4JEmNssQlSWqUJS5JUqMscUmSGmWJS1uwTHhGrXRn1Tt3mvtYk2TH/vLy4VNLWs8Sl7ZQ/SFJPwF8sqr2AB5Kd9a0N4wtN+Phmavq6VX1E2BHwBKX5tFSO3a6pMltcEatJK+iO/nKdXTHrt4WuBfdiWV2SPJPwJ7Al4GXV9VdSb5LdzjJNwG798cL/1x1h5OVNCBLXNpyTXlGrSQ30L03PIbuXMc/7g97eQCwF90hLz9Dd/Sp0ZM8nAD8QU1xEiJJw3BzurTlmu2MeJ+r7jSQ611QVddWd57pM+mOhy9pAVni0pZrpjNq3Qn8fGz58cL3mM3SArPEpS3XtGfUAqY6o9YBSVb1Z117HvB/xub/jO6EQ5LmiSUubaGqO/vRs4DnJrka+A7wK7rTI07l63Q7r11Gd5amfxq7vx8BX01yWZKTBgsu6bc8i5kkSY1yTVySpEZZ4pIkNcoSlySpUZa4JEmNssQlSWqUJS5JUqMscUmSGmWJS5LUqP8PC65rc4K/zjwAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# HINT use groupby method on Orbit column and get the mean of Class column\n",
    "data = df[['Orbit', 'Class']].groupby('Orbit', as_index=False).mean()\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(8,5))\n",
    "sns.barplot(x=\"Orbit\", y=\"Class\", data=data)\n",
    "plt.ylabel(\"Sucess Rate\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Analyze the ploted bar chart try to find which orbits have high sucess rate.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK  4: Visualize the relationship between FlightNumber and Orbit type\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For each orbit, we want to see if there is any relationship between FlightNumber and Orbit type.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1122.38x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value\n",
    "sns.catplot(x=\"FlightNumber\", y=\"Orbit\", hue=\"Class\", data=df, aspect=3)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You should see that in the LEO orbit the Success appears related to the number of flights; on the other hand, there seems to be no relationship between flight number when in GTO orbit.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK  5: Visualize the relationship between Payload and Orbit type\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Similarly, we can plot the Payload vs. Orbit scatter point charts to reveal the relationship between Payload and Orbit type\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1122.38x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value\n",
    "sns.catplot(x=\"PayloadMass\", y=\"Orbit\", hue=\"Class\", data=df, aspect=3)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "With heavy payloads the successful landing or positive landing rate are more for Polar,LEO and ISS.\n",
    "\n",
    "However for GTO we cannot distinguish this well as both positive landing rate and negative landing(unsuccessful mission) are both there here.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK  6: Visualize the launch success yearly trend\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can plot a line chart with x axis to be <code>Year</code> and y axis to be average success rate, to get the average launch success trend.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The function will help you get the year from the date:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A function to Extract years from the date \n",
    "year=[]\n",
    "def Extract_year(date):\n",
    "    for i in df[\"Date\"]:\n",
    "        year.append(i.split(\"-\")[0])\n",
    "    return year\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>Date</th>\n",
       "      <th>BoosterVersion</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Orbit</th>\n",
       "      <th>LaunchSite</th>\n",
       "      <th>Outcome</th>\n",
       "      <th>Flights</th>\n",
       "      <th>GridFins</th>\n",
       "      <th>Reused</th>\n",
       "      <th>Legs</th>\n",
       "      <th>LandingPad</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Serial</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Class</th>\n",
       "      <th>Year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2010-06-04</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>6104.959412</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0003</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "      <td>2010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2012-05-22</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>525.000000</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0005</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "      <td>2012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2013-03-01</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>677.000000</td>\n",
       "      <td>ISS</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0007</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2013-09-29</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>PO</td>\n",
       "      <td>VAFB SLC 4E</td>\n",
       "      <td>False Ocean</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1003</td>\n",
       "      <td>-120.610829</td>\n",
       "      <td>34.632093</td>\n",
       "      <td>0</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2013-12-03</td>\n",
       "      <td>Falcon 9</td>\n",
       "      <td>3170.000000</td>\n",
       "      <td>GTO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>None None</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1004</td>\n",
       "      <td>-80.577366</td>\n",
       "      <td>28.561857</td>\n",
       "      <td>0</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   FlightNumber        Date BoosterVersion  PayloadMass Orbit    LaunchSite  \\\n",
       "0             1  2010-06-04       Falcon 9  6104.959412   LEO  CCAFS SLC 40   \n",
       "1             2  2012-05-22       Falcon 9   525.000000   LEO  CCAFS SLC 40   \n",
       "2             3  2013-03-01       Falcon 9   677.000000   ISS  CCAFS SLC 40   \n",
       "3             4  2013-09-29       Falcon 9   500.000000    PO   VAFB SLC 4E   \n",
       "4             5  2013-12-03       Falcon 9  3170.000000   GTO  CCAFS SLC 40   \n",
       "\n",
       "       Outcome  Flights  GridFins  Reused   Legs LandingPad  Block  \\\n",
       "0    None None        1     False   False  False        NaN    1.0   \n",
       "1    None None        1     False   False  False        NaN    1.0   \n",
       "2    None None        1     False   False  False        NaN    1.0   \n",
       "3  False Ocean        1     False   False  False        NaN    1.0   \n",
       "4    None None        1     False   False  False        NaN    1.0   \n",
       "\n",
       "   ReusedCount Serial   Longitude   Latitude  Class  Year  \n",
       "0            0  B0003  -80.577366  28.561857      0  2010  \n",
       "1            0  B0005  -80.577366  28.561857      0  2012  \n",
       "2            0  B0007  -80.577366  28.561857      0  2013  \n",
       "3            0  B1003 -120.610829  34.632093      0  2013  \n",
       "4            0  B1004  -80.577366  28.561857      0  2013  "
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Extract_year('')\n",
    "    \n",
    "df['Year'] = year\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Year', ylabel='Avg Success Rate'>"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a line chart with x axis to be the extracted year and y axis to be the success rate\n",
    "df[['Year', 'Class']].groupby('Year', as_index=False).mean().plot(kind='line', x='Year', y='Class', ylabel='Avg Success Rate')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = df[['Year', 'Class']].groupby('Year', as_index=False).mean()\n",
    "data.rename(columns={'Class': 'Avg Success Rate'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Year', ylabel='Avg Success Rate'>"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAEGCAYAAABo25JHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAqAklEQVR4nO3deXhU9fn38fdNwr7vW4CAbILKDloVFUSwdRf31lZbqX3Uurf293T7PXbTqlXcELVabV1waUVFUFHABZR9JxDCkrAoBGRJAiHJ/fwxg40RyCTk5GRmPq/rysXMmTNnPiSTuXO+55z7a+6OiIgkr1phBxARkXCpEIiIJDkVAhGRJKdCICKS5FQIRESSXGrYASqqVatWnp6eHnYMEZG4Mn/+/O3u3vpQj8VdIUhPT2fevHlhxxARiStmtuFwj2loSEQkyakQiIgkORUCEZEkp0IgIpLkVAhERJKcCoGISJJTIRARSXIqBCIiR/Dp2u28sWgTBYXFYUcJTNxdUCYiUl1y9+7nun/MI6+wmEZ1UznnhPaMHZTGoC7NMbOw41UZFQIRkcN49MO1FBwo5m+X9eOTzFwmL97MS3Oz6dqqIWMHpXHhgI50aFY/7JhHzeJthrLBgwe7WkyISNByduYz4r6ZXDigI/eMPQGAvP1FvLNsK6/My+azdTswg1O6t2LsoDRG921HvdopIac+PDOb7+6DD/WY9ghERA7hb++tAYObz+zx9bKGdVMZOyiNsYPS2Jibz2sLcnh1fg43v7SIxnVTOadfB8YOSmNg52ZxNXSkQiAiUkbG1j28vjCH607tdtihn84tG3DrqJ7cPLIHc9bl8ur8HP6zcBMvfr6Rbq0jQ0cXDUijXdN61Zy+4jQ0JCJSxk/+MY/PsnKZ9YszaN6wTszP27u/iClLtvDq/Bw+X7+DWgan9GjNJYPSGNWnbahDRxoaEhGJ0fwNO3h/5RfcObpXhYoAQKO6qVw6pBOXDunE+u15vL4gh9cWbOKmFxfSpF4q50aHjvp3qllDR9ojEBGJcncue2IO63LzmHnn6TSoc/R/K5eUOLOzIkNH7yzbwr4DJXRv0+jrs47aNqmeoaMj7RGoEIiIRH246kuueXYud19wHD84sUuVb3/PvgO8HR06mrdhJ7UMhvdszdhBaZx5bLBDRyoEIiLlKClxvjv+IwoOFPP+badROyXYxgtZ2/by2oIcXl+wiS279tG0fm3Oiw4dnZDWtMqHjnSMQESkHJMXb2bV1j08dHn/wIsAQLfWjbhzdG9uG9WLT9du59X5OUyal83zczbQs21k6OiCAR1p0zj4oSPtEYhI0issKmHkAzNoXLc2b910CrVqhXMgd1fBwaGjbBZs/IqUWsZp0aGjkce2oW5q5YeOtEcgInIEL36+kewdBTx7zXGhFQGApvVrc+Wwzlw5rDNrt+3l1fk5vL4ghw9WfUmzBrW59cye/PA76VX+uioEIpLU8vYX8fAHazixWwtO69k67DhfO6Z1I345pjd3nNWLjzMjQ0dN69cO5LVUCETkGz5Y9QXPfLKehy4fQIsKnkcfj57+eB3b9xYy8ereNerc/oMODg8FWaQ0H4GIfC17Rz43v7SIj9Zs59f/WUq8HUOsqB15hUyclcXovm0Z2Ll52HFCo0IgIkDkgOmNLy4Eh6tP6sKUpVv5z6JNYccK1KMfZpJfWMSdo3uFHSVUGhoSEQDuezeDxdlf8eiVAxlzXDtWbN7Nb/+znKFdW9IxAXrul7XpqwKen72BsYPS6N6mcdhxQqU9AhHhw4wvmTgri6uGdeZ7J7QnpZZx/6X9KHbnjkmLKSlJvCGiv723OtpmumfYUUIXaCEwszFmlmFmmWZ21yEeb2pmb5rZYjNbbmbXBJlHRL5t66593D5pMb3bNeY35/T5enmXlg357Tl9mJ2VyzOfrg8vYABWf7GH1xfkcPWJXRJyb6eiAisEZpYCPAqcDfQBrjCzPmVWuwFY4e79gNOB+80s8U9TEKkhikucW15eSEFhMY9cOfBbvW4uG9KJM49twz1TV7H6iz0hpax6f52WQcM6qdxwRvewo9QIQe4RDAUy3T3L3QuBl4Dzy6zjQGOLnLPVCNgBFAWYSURKefiDNczJ2sHdFxxH9zaNvvW4mfHni06gUd1Ubn15EYVFJSGkrFrzN+zkvRVfMG54twq3mU5UQRaCjkB2qfs50WWlPQIcC2wGlgI3u/u33mlmNs7M5pnZvG3btgWVVySpzF6by/jpa7hoQEfGDko77HqtG9flzxcdz/LNuxk/fU01Jqx67s49U1fRqlFdrj2la9hxaowgC8Ghrswoe8RpNLAI6AD0Bx4xsybfepL7RHcf7O6DW7euOVf+icSr3L37ufmlhaS3bMjdFxxX7vqj+7Zj7KA0HpuRyfwNO6ohYTBmrN7G5+t28POR3WlYVydNHhRkIcgBOpW6n0bkL//SrgFe94hMYB3QO8BMIkmvpMS5/ZXFfFVwgIevHBDzB+Lvzu1D+6b1uW3SYvL2x98IbkmJc+/UDDq3aMDlQzqHHadGCbIQzAV6mFnX6AHgy4HJZdbZCIwEMLO2QC8gK8BMIknvqY+zmJGxjV9/71j6dmga8/Ma16vNA5f2Y+OOfP44ZWWACYPx5pLNrNyym9vP6kmdVJ05X1pg3w13LwJuBKYBK4FJ7r7czK43s+ujq90NfMfMlgLTgV+6+/agMokku4Ubd3Lv1AzG9G1XqRm4hnVryXWnduOFzzbywaovAkgYjMKiEu5/dzXHtm/CuSd0CDtOjRPoIJm7TwGmlFk2odTtzcBZQWYQkYhdBQe46cWFtG1Sj3vGnlDpBmu3n9WTWau38YtXl/Lurc3jojHdS3M3snFHPs9cMyTUNtM1lfaPRJKAu3PXa0vYumsfD1854KjaGddNTeGBS/uzq6CQ/3m95jemy9tfxPjpmQzt2oLTa1Cb6ZpEhUAkCfzzs428s2wrd4zuVSVdNvt0aMJto3oxdflWXl9QsxvTPfPJOrbv3c8vx9TMNtM1gQqBSIJbsXk3d7+1gtN6tmbcqd2qbLvjhndjSHpzfj95OTk786tsu1VpZ14hT8zMYlSftgzqkrxtpsujQiCSwPL2F3HjiwtoVj9yxk9Vjo+n1DIeuLQ/Je7c8UrNbEz32IxM8tRmulwqBCIJ7LdvLGfd9jwevLw/LRvVrfLtd2rRgN+d25c5WTv4+yfrqnz7R2PTVwX8Y/YGLhqYRs+2yd1mujwqBCIJ6rX5Oby2IIebRvTgO8e0Cux1LhmcxpnHtuXeaRlkbK05jekeen81ONw6Sm2my6NCIJKA1m7by2/eWMawri24eWSPQF/LzPjLxcfTuG4qt9SQxnRrvtjDq/Nz+MFJajMdCxUCkQSz70AxN/xrAfVqp/DQ5QNIqYbz5ls1ijSmW7llNw++vzrw1yvPfe9m0EBtpmOmQiCSYP749kpWbd3D/Zf0o13TetX2umf1bcelg9OYMHMt89aH15hu4cadTFseaTMdDxe71QQqBCIJ5J2lW3h+zgauO7UrZ/RuU+2v/5tz+tChWaQx3d4QGtP9t810HX6sNtMxUyEQSRDZO/L5xWtL6NepGXeODqeJb6QxXX+yd+bzx7dXVPvrz1qznTlZO7hpRA+1ma4AFQKRBHCguISbXlwIwCNXDAi1u+bQri0YN7wbL36ezfSV1deYrqTEueedVXRqUZ8rhqrNdEWoEIgkgPumZbAo+yvuufgEOrVoEHYcbhvVk97tGvPL15aQu3d/tbzmW0u3sGLLbm4f1UttpitI3y2ROPdhxpc8MSuLq4Z15rvHtw87DhBpTPfg5f3ZXVDEr6qhMV2kzXQGvds15rx+ajNdUSoEInHsi937uH3SYnq3a8xvzukTdpxv6N2uCbef1ZN3V3zBq/NzAn2tl+dlsyE3n1+M6aU205WgQiASp4pLnJtfWkhBYTGPXDmQerVTwo70LT85tRtDu7bgf99cQfaOYBrT5RcWMX76Goamt+CMXtV/plQiUCEQiVMPf7CGOVk7uPuC4+jeplHYcQ4ppZZx/yX9ALj9lcUUB9CY7plP1rNtz35+eXYvtZmuJBUCkTg0JyuX8dPXcNGAjowdlBZ2nCPq1KIBvz23D5+v28HTH1ftlOQ78wqZMGMtZx7blkFdWlTptpOJCoFInMndu5+bX1pIesuG3H3BcWHHicklg9I4q09b7pu2mlVbd1fZdh+fuZa9ajN91FQIROJISYlz+yuL2Zl/gIevHBA3F02ZGX++6Hia1E/l1pcXs7+o+Ki3uWVXAc9+up6LBqTRq53aTB8NFQKROPLUx1nMyNjGb753LH07NA07ToW0bFSXv1x0Aiu37OZv76056u09+N6aaJvpYLurJgMVApE4sXDjTu6dmsHZx7Xj+yd2CTtOpZzZpy2XD+nEE7PWMvcoGtNlfrmXV+Zn8/0Tu5DWPPwL6OKdCoFIHNhVcICbXlxI2yb1+MvFJ8T12TG/PqcPac3rc9ukRZVuTHfftAzq107hhjOOqeJ0yUmFQKSGc3d+9foStu7ax8NXDqBp/dphRzoqjeqm8rdL+7NpZwF3v1nxxnSLsr9i6vKtXDe8WyDTbyYjFQKRGu5fn21kytKt3Dm6FwM7Nw87TpUYnN6Cn552DC/Py+a9FbE3pnOPNJZr2bAOPzm1W4AJk4sKgUgNtnLLbv7fWys4vVdrrkuwD75bz+zJse2bcNdrS9geY2O6j9ZsZ3ZWLjeO6E6jODljKh6oEIjUUHn7i7jhhQU0q1+b+y/pl3A9dOqk1uLBy/qzZ19sjelKSpx7p60irXl9rhymNtNVSYVApIb67RvLWbc9jwcv75+wY+G92jXmztG9eG/FF7xSTmO6t5duYdmm3dw2qid1U2teX6V4pkIgUgO9viCH1xbkcNOIHnznmFZhxwnUj0/pyrCuLfjfycsP25juQPF/20yf379jNSdMfDEVAjOrb2a6hlukGqzdtpdf/2cZw7q24OaRiX+xVK1axv2X9sPMuH3SoRvTvTw3m/W5+dw5uhcpCTZEVhOUWwjM7FxgETA1er+/mU0OOJdIUtp3oJgbX1hIvdopPHT5gKT50Etr3oDfn9eXz9fv4KmPvtmYrqCwmIemr2Fwl+aM6K0200GIZY/g98BQ4CsAd18EpAcVSCSZ/fHtlazcspv7L+lHu6b1wo5TrS4e2JExfdtx/7urWbnlv43pnvl0XbTNdO+4vpCuJoulEBS5+67Ak4gkuU8yt/P8nA1cd2pXzkjCv3zNjD9ddDxN6tfm1pcXsb+omK/yC3l8xlpG9m7DkHS1mQ5KLCfiLjOzK4EUM+sB/Bz4NNhYIsnF3bl36io6NqvPHUncUrlFwzrcO/Z4rn12Hg+8txqAvfuLuHNM8n5PqkMsewQ3AX2B/cALwC7g5iBDiSSbacu3sjhnF7ec2SPpT40c0bstVwztzMRZWTzz8Xou7N+R3u2ahB0rocVSCL7n7v/X3YdEv34NnBfLxs1sjJllmFmmmd11mHVON7NFZrbczGZWJLxIIigqLuG+d1fTvU0jLhpYs2cbqy6//t6xdG7RAMe5dVTPsOMkvFiGhn4FvBLDsm8wsxTgUWAUkAPMNbPJ7r6i1DrNgMeAMe6+0cySb2BUkt7rCzeR+eVeJnx/YNKcJVSehnVTeeG6E9m6q4BOLdRmOmiHLQRmdjbwXaCjmY0v9VATIJbesUOBTHfPim7vJeB8oHS7wSuB1919I4C7f1mx+CLxbX9RMQ+9v4Z+aU0Z3bdd2HFqlI7N6tOxWf2wYySFIw0NbQbmAfuA+aW+JgOjY9h2RyC71P2c6LLSegLNzWyGmc03s6sPtSEzG2dm88xs3rZt22J4aZH48K85G9n0VQF3jtapkRKew+4RuPtiYLGZveDuByqx7UO9q8teMpgKDAJGAvWB2WY2x91Xl8kyEZgIMHjw4CN3phKJE3v3F/Hoh5mc3L0lp/RI7DYSUrPFcowg3cz+DPQBvr7Cxd3L64mbA3QqdT+NyF5G2XW2u3sekGdms4B+wGpEEtzfP15Hbl4hd47uHXYUSXKxnDX0DPA4keMCZwDPAc/H8Ly5QA8z62pmdYDLiQwrlfYGcKqZpZpZA2AYsDLW8CLxamdeIU/OymJ037b079Qs7DiS5GIpBPXdfTpg7r7B3X8PjCjvSe5eBNwITCPy4T7J3Zeb2fVmdn10nZVEehgtAT4HnnL3ZZX7r4jEj8dnriWvsIg7ztKFUhK+WIaG9plZLWCNmd0IbAJiOs3T3acAU8osm1Dm/l+Bv8YWVyT+bdlVwLOfrufCAWn0aNs47DgiMe0R3AI0INJaYhDwA+CQZ/eISPnGT1+Du3PLmYnfYlriQ7l7BO4+N3pzL3CNmaUClwGfBRlMJBFlbdvLpHk5/ODELrpQSmqMw+4RmFkTM/uVmT1iZmdZxI1AJnBp9UUUSRwPvLeauqm1uOGM7mFHEfnakfYIngd2ArOBnwB3AnWAC6JzEohIBSzbtIu3lmzhphHdad04Mecglvh0pELQzd2PBzCzp4DtQGd331MtyUQSzH3vZtCsQW2uG17eJTgi1etIB4u/vprY3YuBdSoCIpXzWVYuMzK28bPTjqFJvdphxxH5hiPtEfQzs4PzxRlQP3rfAHd3NQgXiYG7c++0DNo2qcsPv5MedhyRbzlSr6Hknh1DpIp8sOpL5m/YyR8vPI56tfVrJTVPLNcRiEgllZQ4f52WQXrLBlw6uFP5TxAJgQqBSIDeXLKZVVv3cOuontRO0a+b1Ex6Z4oE5EBxCQ+8t5pj2zfh3BM6hB1H5LDKLQRm1jDaawgz62lm55mZTnsQKcfLc7PZkJvPL0b3opamoJQaLJY9gllAPTPrCEwHrgGeDTKUSLwrKCxm/PQ1DElvzum9WocdR+SIYikE5u75wEXAw+5+IZFJakTkMJ79dD1f7tnPL8ZoCkqp+WIqBGZ2EnAV8HZ0WSztq0WS0q6CA0yYuZYzerVmSHqLsOOIlCvWNtS/Av4dnVimG/BhoKlE4tjEWWvZVXCAO0Zr0hmJD7G0oZ4JzASIHjTe7u4/DzqYSDz6cs8+/v7xes7t14G+HZqGHUckJrGcNfRCtCV1Q2AFkGFmdwYfTST+PPpBJgeKS7h9VM+wo4jELJahoT7uvhu4gMi0k52JzFImIqVk78jnhc83cumQTqS3ahh2HJGYxVIIakevG7gAeMPdDwAeaCqROPS391ZTy4yfj9AUlBJfYikETwDrgYbALDPrAuw+4jNEkkzG1j38e9EmfvSddNo1rRd2HJEKieVg8XhgfKlFG8zsjOAiicSf+97NoFGdVK4/7Ziwo4hUWCwHi9ua2dNm9k70fh/gh4EnE4kTCzbu5L0VXzBueDeaN6wTdhyRCotlaOhZYBpwsGvWaiLXFogkPXfnr1MzaNWoDtee0jXsOCKVEkshaOXuk4ASAHcvAooDTSUSJz7O3M7srFxuOKM7DevqgnuJT7EUgjwza0n0TCEzOxHYFWgqkTjg7tw7NYOOzepz5bDOYccRqbRY/oS5DZgMHGNmnwCtgbGBphKJA+8s28rSTbu475J+1E3VFJQSv2I5a2iBmZ0G9CIycX1G9FoCkaRVVFzCfe9m0KNNIy4c0DHsOCJHJZazhm4AGrn7cndfBjQys/8TfDSRmuv1BZvI2pbH7Wf1IkWTzkici+UYwXXu/tXBO+6+E7gusEQiNdy+A8U8+P5q+nVqxui+bcOOI3LUYikEtazUzBpmlgLoZGlJWv/6bCObd+3jF6N7adIZSQixHCyeBkwyswlEzhy6HpgaaCqRGmrv/iIe/TCTk7u35OTurcKOI1IlYikEvwTGAT8jcrD4XeCpIEOJ1FRPfZTFjrxC7hzdO+woIlUmlkJQH3jS3SfA10NDdYH8IIOJ1DQ78gp56qN1jOnbjv6dmoUdR6TKxHKMYDqRYnBQfeD9YOKI1FyPfZhJfmERd4zWpDOSWGIpBPXcfe/BO9HbDWLZuJmNMbMMM8s0s7uOsN4QMys2M12oJjXS5q8KeG7OBi4amEb3No3DjiNSpWJtMTHw4B0zGwQUlPek6BDSo8DZQB/gimjn0kOtdw+Rg9IiNdL46WvA4ZYzNemMJJ5YjhHcArxiZpuj99sDl8XwvKFAprtnAZjZS8D5ROY9Lu0m4DVgSCyBRarb2m17mTQvm6tPSieteUw7wyJxJZYWE3PNrDf/bTGxKsYWEx2B7FL3c4BhpVcws47AhcAIjlAIzGwckTOX6NxZzb2kej3w7mrq1U7hxhHdw44iEohyC4GZXV1m0QAzw92fK++ph1hWdq7jB4FfunvxkS7McfeJwESAwYMHa75kqTbLNu3i7aVbuGlEd1o1qht2HJFAxDI0VPov9XrASGABUF4hyAE6lbqfBmwus85g4KVoEWgFfNfMitz9PzHkEgncvdMyaNagNtcN7xZ2FJHAxDI0dFPp+2bWFHg+hm3PBXqYWVdgE3A5cGWZbX89pZOZPQu8pSIgNcWcrFxmrd7G/3y3N03q1Q47jkhgKjOlUj5Q7qkT7l5kZjcSORsoBfi7uy83s+ujj0+oxGuLVIvIpDOraNekHleflB52HJFAxXKM4E3+O7afAhwLTIpl4+4+BZhSZtkhC4C7/yiWbYpUh+krv2TBxq/404XHU6+2Jp2RxBbLHsF9pW4XARvcPSegPCKhKy5x/jotg/SWDbhkcFrYcUQCF8sxgpkA0XmLhwP7iBwIFklIkxdvIuOLPYy/YgC1U2K55lIkvh32XW5mb5nZcdHb7YFlwLXA82Z2S/XEE6lehUUlPPDeavq0b8I5x7cPO45ItTjSnztdo1NTAlwDvOfu5xK5KOzawJOJhODluRvJ3lHAnaN7UUtTUEqSOFIhKH318EiiB33dfQ9QEmQokTDkFxYx/oNMhqa34PRercOOI1JtjnSMINvMbiJyPGAg0VnJzKw+oJOqJeE8++l6tu3Zz+NXDdQUlJJUjrRH8GOgL/Aj4LJSE9ifCDwTbCyR6rUr/wATZqxlRO82DE5vEXYckWp12D0Cd/+SyPzEZZd/CHwYZChJHsUlzr4DxWHH4LGZmezeV8QdZ/UKO4pItavMlcUiVaK4xPne+I9YtXVP2FEAOK9fB/p0aBJ2DJFqp0IgoXl3+VZWbd3D1Sd1Ia15/fKfEKBaZlwwoGOoGUTCokIgoXB3JsxcS5eWDfjduX1J0amaIqGJpdfQ+EMs3gXMc/c3qj6SJIPP1u1gcc4u/nDBcSoCIiGLafJ6oD+wJvp1AtAC+LGZPRhYMkloE2aupVWjOowdpF4+ImGLZWioOzDC3YsAzOxx4F1gFLA0wGySoFZu2c2MjG3ccVZPdfYUqQFi2SPoCDQsdb8h0MHdi4H9gaSShPbkrCwa1Enh+yd2CTuKiBDbHsG9wCIzm0FkHuLhwJ/MrCHwfoDZJAFt+qqAyYs3c/VJ6TRrUCfsOCJCbG2onzazKcBQIoXgf9z94NzDdwYZThLP0x+tA+DHp3YtZ00RqS6xnDU0GXgRmOzuecFHkkT1VX4hL83dyHn9OtCxWbjXDYjIf8VyjOB+4FRghZm9YmZjzaxewLkkAf1zzgbyC4sZd1q3sKOISCmxzlA208xSgBHAdcDfAV2LLzHbd6CYZz9dz+m9WtO7nd46IjVJTFcWR1tPnwtcRqQl9T+CDCWJ59X5OWzfW8j1px0TdhQRKSOWYwQvE5mVbCrwKDDD3TUxjcSsuMR58qMs+nVqxrCuavEsUtPEcozgGeAYd7/e3T8ATjKzRwPOJQlk2vKtbMjN5/rh3TThi0gNFMsxgqlm1t/MriAyNLQOeD3wZJIQ3J0nZq6la6uGnNW3XdhxROQQDlsIzKwncDlwBZALvAyYu59RTdkkAczOymVxzi7+dOHxai4nUkMdaY9gFfARcK67ZwKY2a3VkkoSxhMzs2jVqA4XDVSvf5Ga6kjHCC4GtgIfmtmTZjaSyJXFIjFZuWU3M1dv45qTu6q5nEgNdthC4O7/dvfLgN7ADOBWoK2ZPW5mZ1VTPoljE2dl0bBOCt8fpuZyIjVZuWcNuXueu//L3c8B0oBFwF1BB5P4lrMzn8mLN3PF0M40bVA77DgicgSxnD76NXff4e5PuPuIoAJJYnj643UYcO0pai4nUtNVqBCIxGJnXiEvfZ7Nef070EHN5URqPBUCqXL/nLOBggPF/HS42kmIxAMVAqlSB5vLjejdhl7tGocdR0RioEIgVeqV+Tnk5hXy0+FqNS0SL1QIpMoUlzhPzsqif6dmDFVzOZG4EWghMLMxZpZhZplm9q1TTs3sKjNbEv361Mz6BZlHgjV12VY27sjn+tPUXE4kngRWCKIT2TwKnA30Aa4wsz5lVlsHnObuJwB3AxODyiPBcncmzFxLt1YNGdVHzeVE4kmQewRDgUx3z3L3QuAl4PzSK7j7p+6+M3p3DpEL1iQOzV6by9JNu7hueDc1lxOJM0EWgo5Adqn7OdFlh/Nj4J1DPWBm48xsnpnN27ZtWxVGlKoyYVYWrRrV5cIBai4nEm+CLASH+rPQD7mi2RlECsEvD/W4u09098HuPrh169ZVGFGqworNu5m1ehvXnJyu5nIicSimOYsrKQfoVOp+GrC57EpmdgLwFHC2u+cGmEcC8sSstZHmciequZxIPApyj2Au0MPMuppZHSKT3EwuvYKZdSYy29kP3H11gFkkINk78nlryRauHNaZpvXVXE4kHgW2R+DuRWZ2IzANSAH+7u7Lzez66OMTgN8CLYHHoqcbFrn74KAySdVTczmR+Bfk0BDuPgWYUmbZhFK3fwL8JMgMEpydeYW8PDeb8/t3pH1TNZcTiVe6slgq7bnZ0eZyp6mdhEg8UyGQSikoLOYfs9czsncberZVczmReKZCIJXy6vxsduQV8tPT1GpaJN6pEEiFFRWX8ORH6xjQuRlD0puHHUdEjpIKgVTYO183lztGzeVEEoAKgVSIu/PErGhzuWPbhh1HRKqACoFUyKdrc1m2aTfjhnejlprLiSQEFQKpkAkz19K6cV0uUHM5kYShQiAxW7ZpFx+t2c61J3dVczmRBKJCIDGbOCuLRnVTuXJY57CjiEgVUiGQmGTvyOftpWouJ5KIVAgkJk9/vI5aBteerOZyIolGhUDKtSOvkJfmbuSC/h1p17Re2HFEpIqpEEi5npu9nn0HShg3XM3lRBKRCoEcUUFhMf/4dD1nHtuGHmouJ5KQVAjkiF6Zn83O/ANqLieSwFQI5LCKikuYOCuLQV2aMyS9RdhxRCQgKgRyWFOWbSVnZwE/1bEBkYSmQiCH5O48MXMt3Vo35Ew1lxNJaCoEckifZOayfPNufqrmciIJT4VADmnCzLW0UXM5kaSgQiDfsmzTLj7O3M61p3Slbqqay4kkOhUC+ZYn1FxOJKmoEMg3ZO/I5+0lm7lqWGea1FNzOZFkoEIg3/DkR1mk1DKuPUXN5USShQqBfC13734mzcvmwgEdadtEzeVEkoUKgXztudkb1FxOJAmpEAgA+YVFPDd7PWce25bubdRcTiSZqBAIAJPmRprL/ex07Q2IJBsVAqGouIQnP1rH4C7NGdRFzeVEko0KgfD20i1s+qpAraZFkpQKQZKLNJfLonubRozs3SbsOCISAhWCJPfRmu2s2LKbcWouJ5K0VAiS3BOz1tK2SV3O798h7CgiEhIVgiS2NGcXn2Tmcu3Jai4nkswCLQRmNsbMMsws08zuOsTjZmbjo48vMbOBQeaRb3pi1loa103lCjWXE0lqgRUCM0sBHgXOBvoAV5hZnzKrnQ30iH6NAx4PKo9804bcPKYs3cJVJ3ZRczmRJJca4LaHApnungVgZi8B5wMrSq1zPvCcuzswx8yamVl7d99S1WFmrt7GH95aUf6KSWJXwQFSa9XimpPTw44iIiELshB0BLJL3c8BhsWwTkfgG4XAzMYR2WOgc+fKDWM0qptKj7aNKvXcRHVy91ZqLicigRaCQ52L6JVYB3efCEwEGDx48Lcej8WgLs0Z1GVQZZ4qIpLQgjxYnAN0KnU/DdhciXVERCRAQRaCuUAPM+tqZnWAy4HJZdaZDFwdPXvoRGBXEMcHRETk8AIbGnL3IjO7EZgGpAB/d/flZnZ99PEJwBTgu0AmkA9cE1QeERE5tCCPEeDuU4h82JdeNqHUbQduCDKDiIgcma4sFhFJcioEIiJJToVARCTJqRCIiCQ5ixyvjR9mtg3YUMmntwK2V2GcylKOb1KOb6oJOWpCBlCOso4mRxd3b32oB+KuEBwNM5vn7oOVQzmUo+ZnUI7qy6GhIRGRJKdCICKS5JKtEEwMO0CUcnyTcnxTTchREzKAcpQVSI6kOkYgIiLflmx7BCIiUoYKgYhIkovrQmBmnczsQzNbaWbLzezm6PIWZvaema2J/ts8urxldP29ZvZImW0NMrOlZpZpZuPN7FCT5gSaw8wamNnbZrYqup2/hPj9mGpmi6PbmRCdg7rac5Ta5mQzWxbi92OGmWWY2aLoV5uQctQxs4lmtjr6Prm4OjOYWeNS34NFZrbdzB4M6XtxhUV+Z5dE36+tQspxWTTDcjO7N9YMlcwxyszmR//f881sRKltVfozDHeP2y+gPTAwersxsBroA9wL3BVdfhdwT/R2Q+AU4HrgkTLb+hw4icisae8AZ1d3DqABcEb0dh3gozByRB9rEv3XgNeAy8PIEX38IuAFYFmI748ZwOAa8D79X+AP0du1gFZh/ExKbXc+MDyE35VU4MuD///o838fQo6WwEagdfT+P4CRAeYYAHSI3j4O2FRqW5X/DKvMG7umfgFvAKOADKB9qW90Rpn1flTmh9keWFXq/hXAE9Wd4xDbeQi4LswcQG3gTeCyMHIAjYCPo78cFSoEVZxjBpUsBFWcIxtoGGaGUo/1iOax6s4RfV9uA7oQ+eCbAIwLIccQ4P1S938APBZ0juhyA3KBuhzlZ1hcDw2VZmbpRKrlZ0Bbj850Fv23vN34jkSmzTwoJ7qsunOU3k4z4Fxgelg5zGwakb+69gCvhpTjbuB+IhMXVVoV/VyeiQ6H/KZCu91VlCP6ngC428wWmNkrZta2OjOUcQXwskc/eaozh7sfAH4GLCUyvW0f4OnqzkFkUq3eZpZuZqnABXxz+t0gc1wMLHT3/RzlZ1hCFAIza0Rk+OIWd99dmU0cYlmF39xVkOPgdlKBF4Hx7p4VVg53H03kL426wIhyVq/yHGbWH+ju7v+u6HOrMkfUVe5+PHBq9OsHIeRIJTKv9yfuPhCYDdxXzRlKu5zI+7TCquC9UZtIIRgAdACWAL+q7hzuvjOa42UiQ7nrgaKgc5hZX+Ae4KcHFx0qXqyvH/eFIPqGeA34l7u/Hl38hZm1jz7enshftUeSQ+QX7KA0In9lVHeOgyYCa9z9wYpkCCAH7r6PyNzS54eQ4yRgkJmtJzI81NPMZoSQA3ffFP13D5HjFUNDyJFLZM/oYGF8BRhYzRkObqsfkOru82N9/SrO0R/A3ddG90gmAd8JIQfu/qa7D3P3k4gM6awJMoeZpRF5D1zt7muji4/qMyyuC0F09/xpYKW7P1DqocnAD6O3f0hk3O2wortee8zsxOg2ry7vOUHkiG7rD0BT4JZYX7+qc5hZo1JvwlQi80qvqu4c7v64u3dw93QiB+pWu/vp1Z3DzFIPnpES/aU9B4j5DKYq/H44keM1p0cXjQRWVGeGUq6gEnsDVZhjE9DHzA520xwFrAwhBxY9gyx6Zs//AZ4KKkd0ePBt4Ffu/snBlY/2M+yoDjiF/UXkw8GJ7BYuin59l8iR/OlEKvN0oEWp56wHdgB7iVTRPtHlg4n8cq8FHqECB8CqKgeRKu5E3tAHt/OTEHK0BeZGt7MceJjIX3/V/nMp9Xg6FT9rqKq+Hw2JnB1z8PvxEJAS0vu0CzAruq3pQOcwfiZAFtA75N/Z64n8riwhUiBbhpTjRSIFeQUVOLuuMjmAXwN5pdZdBLQ52s8wtZgQEUlycT00JCIiR0+FQEQkyakQiIgkORUCEZEkp0IgIpLkVAhEymERH5vZ2aWWXWpmU8PMJVJVdPqoSAzM7DgiV/IOAFKInL89xv97ZWdFtpXi7sVVm1Ck8lQIRGJkkV7zeUQuMMsjcnHX8UR6AP3e3d+INg57ProOwI3u/qmZnQ78DtgC9Hf3PtWbXuTwVAhEYmRmDYEFQCHwFrDc3f8Zvez/cyJ7Cw6UuPs+M+sBvOjug6OF4G3gOHdfF0Z+kcNJDTuASLxw9zwze5lIi4FLgXPN7I7ow/WAzkQafT0S7ZxaDPQstYnPVQSkJlIhEKmYkuiXARe7e0bpB83s98AXQD8iJ2PsK/VwXjVlFKkQnTUkUjnTgJsOTlBjZgOiy5sCW9y9hMicBTHP9SwSFhUCkcq5m8h0iUvMbFn0PsBjwA/NbA6RYSHtBUiNp4PFIiJJTnsEIiJJToVARCTJqRCIiCQ5FQIRkSSnQiAikuRUCEREkpwKgYhIkvv/2rrZu3s+b50AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lineplot(x='Year', y='Avg Success Rate', data=data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "you can observe that the sucess rate since 2013 kept increasing till 2020\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Features Engineering\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By now, you should obtain some preliminary insights about how each important variable would affect the success rate, we will select the features that will be used in success prediction in the future module.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>FlightNumber</th>\n",
       "      <th>PayloadMass</th>\n",
       "      <th>Orbit</th>\n",
       "      <th>LaunchSite</th>\n",
       "      <th>Flights</th>\n",
       "      <th>GridFins</th>\n",
       "      <th>Reused</th>\n",
       "      <th>Legs</th>\n",
       "      <th>LandingPad</th>\n",
       "      <th>Block</th>\n",
       "      <th>ReusedCount</th>\n",
       "      <th>Serial</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>6104.959412</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>525.000000</td>\n",
       "      <td>LEO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>677.000000</td>\n",
       "      <td>ISS</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B0007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>PO</td>\n",
       "      <td>VAFB SLC 4E</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>3170.000000</td>\n",
       "      <td>GTO</td>\n",
       "      <td>CCAFS SLC 40</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>B1004</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   FlightNumber  PayloadMass Orbit    LaunchSite  Flights  GridFins  Reused  \\\n",
       "0             1  6104.959412   LEO  CCAFS SLC 40        1     False   False   \n",
       "1             2   525.000000   LEO  CCAFS SLC 40        1     False   False   \n",
       "2             3   677.000000   ISS  CCAFS SLC 40        1     False   False   \n",
       "3             4   500.000000    PO   VAFB SLC 4E        1     False   False   \n",
       "4             5  3170.000000   GTO  CCAFS SLC 40        1     False   False   \n",
       "\n",
       "    Legs LandingPad  Block  ReusedCount Serial  \n",
       "0  False        NaN    1.0            0  B0003  \n",
       "1  False        NaN    1.0            0  B0005  \n",
       "2  False        NaN    1.0            0  B0007  \n",
       "3  False        NaN    1.0            0  B1003  \n",
       "4  False        NaN    1.0            0  B1004  "
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]\n",
    "features.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK  7: Create dummy variables to categorical columns\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the function <code>get_dummies</code> and <code>features</code> dataframe to apply OneHotEncoder to the column <code>Orbits</code>, <code>LaunchSite</code>, <code>LandingPad</code>, and <code>Serial</code>. Assign the value to the variable <code>features_one_hot</code>, display the results using the method head. Your result dataframe must include all features including the encoded ones.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Orbit_ES-L1</th>\n",
       "      <th>Orbit_GEO</th>\n",
       "      <th>Orbit_GTO</th>\n",
       "      <th>Orbit_HEO</th>\n",
       "      <th>Orbit_ISS</th>\n",
       "      <th>Orbit_LEO</th>\n",
       "      <th>Orbit_MEO</th>\n",
       "      <th>Orbit_PO</th>\n",
       "      <th>Orbit_SO</th>\n",
       "      <th>Orbit_SSO</th>\n",
       "      <th>...</th>\n",
       "      <th>Serial_B1048</th>\n",
       "      <th>Serial_B1049</th>\n",
       "      <th>Serial_B1050</th>\n",
       "      <th>Serial_B1051</th>\n",
       "      <th>Serial_B1054</th>\n",
       "      <th>Serial_B1056</th>\n",
       "      <th>Serial_B1058</th>\n",
       "      <th>Serial_B1059</th>\n",
       "      <th>Serial_B1060</th>\n",
       "      <th>Serial_B1062</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 72 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Orbit_ES-L1  Orbit_GEO  Orbit_GTO  Orbit_HEO  Orbit_ISS  Orbit_LEO  \\\n",
       "0            0          0          0          0          0          1   \n",
       "1            0          0          0          0          0          1   \n",
       "2            0          0          0          0          1          0   \n",
       "3            0          0          0          0          0          0   \n",
       "4            0          0          1          0          0          0   \n",
       "\n",
       "   Orbit_MEO  Orbit_PO  Orbit_SO  Orbit_SSO  ...  Serial_B1048  Serial_B1049  \\\n",
       "0          0         0         0          0  ...             0             0   \n",
       "1          0         0         0          0  ...             0             0   \n",
       "2          0         0         0          0  ...             0             0   \n",
       "3          0         1         0          0  ...             0             0   \n",
       "4          0         0         0          0  ...             0             0   \n",
       "\n",
       "   Serial_B1050  Serial_B1051  Serial_B1054  Serial_B1056  Serial_B1058  \\\n",
       "0             0             0             0             0             0   \n",
       "1             0             0             0             0             0   \n",
       "2             0             0             0             0             0   \n",
       "3             0             0             0             0             0   \n",
       "4             0             0             0             0             0   \n",
       "\n",
       "   Serial_B1059  Serial_B1060  Serial_B1062  \n",
       "0             0             0             0  \n",
       "1             0             0             0  \n",
       "2             0             0             0  \n",
       "3             0             0             0  \n",
       "4             0             0             0  \n",
       "\n",
       "[5 rows x 72 columns]"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# HINT: Use get_dummies() function on the categorical columns\n",
    "features_one_hot = pd.get_dummies(df[['Orbit', 'LaunchSite', 'LandingPad', 'Serial']])\n",
    "features_one_hot.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TASK  8: Cast all numeric columns to `float64`\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that our <code>features_one_hot</code> dataframe only contains numbers cast the entire dataframe to variable type <code>float64</code>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HINT: use astype function\n",
    "features_one_hot = features_one_hot.astype('float64')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Orbit_ES-L1     float64\n",
       "Orbit_GEO       float64\n",
       "Orbit_GTO       float64\n",
       "Orbit_HEO       float64\n",
       "Orbit_ISS       float64\n",
       "                 ...   \n",
       "Serial_B1056    float64\n",
       "Serial_B1058    float64\n",
       "Serial_B1059    float64\n",
       "Serial_B1060    float64\n",
       "Serial_B1062    float64\n",
       "Length: 72, dtype: object"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "features_one_hot.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can now export it to a <b>CSV</b> for the next section,but to make the answers consistent, in the next lab we will provide data in a pre-selected date range.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<code>features_one_hot.to_csv('dataset_part\\_3.csv', index=False)</code>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Authors\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a href=\"https://www.linkedin.com/in/nayefaboutayoun/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\">Nayef Abou Tayoun</a> is a Data Scientist at IBM and pursuing a Master of Management in Artificial intelligence degree at Queen's University.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Change Log\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "| Date (YYYY-MM-DD) | Version | Changed By    | Change Description      |\n",
    "| ----------------- | ------- | ------------- | ----------------------- |\n",
    "| 2021-10-12        | 1.1     | Lakshmi Holla | Modified markdown       |\n",
    "| 2020-09-20        | 1.0     | Joseph        | Modified Multiple Areas |\n",
    "| 2020-11-10        | 1.1     | Nayef         | updating the input data |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Copyright © 2020 IBM Corporation. All rights reserved.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

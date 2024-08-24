<h1 style="text-align: center;">Electric Field Simulator</h1>
<p>This program is designed to provide a gui to simulate electric fields in brain using <a href="https://github.com/MatthewFilipovich/pycharge">PyCharge</a>.<br>*note that the calculations are carried out in vacuum space</p>
<p><b>*DISCLAIMER</b>: The ability to put a charge inside the circle which represents the head is a design choice to allow more experimentation.</p>

<h2>Content</h2>
<ul>
    <li><a href = "#usage">Usage</a><ul>
    <li><a href = "#source">From Source (Recommended)</a></li>
    <li><a href = "#exe">From Executable (Windows Only)</a></li>
    </ul>
    </li>
    <li><a href = "#ui">Interface</a></li>
    <li><a href = "#sim">Running a simulation</a></li>
    <li><a href = "#settings">Settings</a></li>
    <li><a href = "#shortcuts">Keyboard Shortcuts</a></li>
    <li><a href = "#issues">Issues</a></li>
</ul>

<h2 id = "usage">Usage</h2>
<h3 id = "source">From Source (Recommended)</h3>
<h4>Prerequisites</h4>
<h4>Step 1 - Python</h4>
<p>First make sure you have Python installed.<br>You can execute <code>python --version</code> to check if you have python installed, if you don't have Python installed you can install it from <a href="https://www.python.org/">this link</a>.</p>

<h4>Step 2 - Libraries</h4>
<p>Execute <code>pip install -r requirements.txt</code> to get all the required libraries.</p>

<h4>Step 3 - Running The Program</h4>
<p>Execute <code>python gui.py</code> to run the program.</p>

<h3 id = "exe">From Executable (Windows Only)</h3>
<p>Windows users can simply download the exe file from releases and use the program.<br>*note that this executable has been created using <a href="https://github.com/brentvollebregt/auto-py-to-exe">auto-py-to-exe</a> and hasn't been tested thoroughly.

<h2 id = "ui">Interface</h2>
<center>
<img src= "screenshots\1.png">
</center>
<p><b>1</b> - This panels lists all the current charges.<br>
<b>2</b> - This is the utility panel of the program.<br>
<b>3</b> - This panel shows a preview of charge positions and head radius.<br>
<b>4</b> - This bar indicates the progress of simulation process.<br></p>

<h2 id = "sim">Running a simulation</h2>
<h4>Adding Charges</h4>
<center>
<img src= "screenshots\4.png">
</center>
<p>You can use the "Add Charge" button or simply click on where you want to add a charge and to do this however <b>this method is not recommended</b>.
<p>Instead use "Load CSV" <b>(Recommended)</b> to load all the charges at once. To do this create a CSV file with columns <code>X,Y,q</code> and load it into the program. you can see an example csv in the repository</p>

<center>
<img src= "screenshots\3.png">
</center>

<h4>Example Input</h4>
<center>
<img src= "screenshots\5.png">
</center>
<h4>Example Output</h4>
<center>
<img src= "screenshots\6.png">
</center>
<h2 id = "settings">Settings</h2>
<center>
<img src= "screenshots\2.png">
</center>

<table>
    <tr>
        <th>Setting</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Head Radius</td>
        <td>Radius of the head in <b>meter</b>.</td>
    </tr>
    <tr>
        <td>Number of simulation points</td>
        <td>Number of simulation points per axis. (100 would result in 10,000 simulation points in total)</td>
    </tr>
    <tr>
        <td>linthresh</td>
        <td>Plotting parameter. Please refer to <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html">matplotlib documentation</a>.</td>
    </tr>
    <tr>
        <td>linscale</td>
        <td>Plotting parameter. Please refer to <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html">matplotlib documentation</a>.</td>
    </tr>
    <tr>
        <td>vmin</td>
        <td>Plotting parameter. Please refer to <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html">matplotlib documentation</a>.</td>
    </tr>
    <tr>
        <td>vmax</td>
        <td>Plotting parameter. Please refer to <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html">matplotlib documentation</a>.</td>
    </tr>
</table>

<h2 id = "shortcuts">Keyboard Shortcuts</h2>
<table>
    <tr>
        <th>Shortcut</th>
        <th>Function</th>
    </tr>
    <tr>
        <td>Enter</td>
        <td>Save (where "Save" button is present).</td>
    </tr>
    <tr>
        <td>Ctrl + A</td>
        <td>Add charge.</td>
    </tr>
    <tr>
        <td>Ctrl + C</td>
        <td>Clear all charges.</td>
    </tr>
    <tr>
        <td>Ctrl + R</td>
        <td>Run simulation.</td>
    </tr>
    <tr>
        <td>Ctrl + L</td>
        <td>Load CSV file.</td>
    </tr>
    <tr>
        <td>F1</td>
        <td>Open settings.</td>
    </tr>
</table>

<h2 id = "issues">Issues</h2>
<p>Please refer to issues tab to see a list of current identified issues.</p>

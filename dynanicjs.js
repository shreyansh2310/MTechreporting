var subjectObject = {
    "M-TECH": {
        "CSE_DEPT": ["Artificial Intelligence (AI)", "Machine Learning (ML)", "Data Science", "Software Engineering", "Cybersecurity", "Cloud Computing", "Information Systems"],
        "ECE_DEPT": ["Micro Electronics", "Integrated Electronics and circuit", "VLSI design tool and technology", "Communication Engineering", "Telecommunication tech and management", "Microwave engineering", "Nanotechnology", "Computer Technology"],
        "EEE_DEPT": ["semiconductors", "nanoelectronics", "electrophysics", "microsystems", "optics and photonics", "signal and image processing"],
        "MECH_DEPT": ["Combustion and the Environment", "Ground Vehicle Systems", "Heat Transfer", "Thermodynamics and Energy Systems", "Manufacturing", "Mechanical Design", "System Dynamics and Control", "Transportation Systems"],
        "CIVIL_DEPT": ["Environmental Engineering", "Geoinformatics", "Geothechnical Engineering", "Hydraulics and Water Resources Engineering", "Infrastructure Engineering and Management", "Structural Engineering", "Transportation Engineering"],
        "CHEM_DEPT": ["pharmaceuticals", "healthcare", "design and construction", "pulp and paper", "petrochemicals", "food processing", "specialty chemicals"],
        "BIOTECH_DEPT": ["Human Biology", "Structural Biochemistry", "Biological Chemistry", "Plant Science", "Microbiology", "Protein Science", "Molecular Genetics", "Metabolism"],
        "MME_DEPT": ["Links", "Images", "Tables", "Lists"],
        "MAT_DEPT": ["applied mathematics", "computational mathematics"],
        "CHE_DEPT": ["Biochemistry", "Geochemistry", "Chemicalphysics", "Chemical engineering", "Environmental science", "Forensic", "Green chemistry"],
        "PHY_DEPT": ["particle physics", "astrophysics", "biotechnology", "meteorology", "nanotechnology"],
    }
}
window.onload = function() {
    var subjectSel = document.getElementById("course");
    var topicSel = document.getElementById("department");
    var chapterSel = document.getElementById("specialization");
    for (var x in subjectObject) {
        subjectSel.options[subjectSel.options.length] = new Option(x, x);
    }
    subjectSel.onchange = function() {
        //empty Chapters- and Topics- dropdowns
        chapterSel.length = 1;
        topicSel.length = 1;
        //display correct values
        for (var y in subjectObject[this.value]) {
            topicSel.options[topicSel.options.length] = new Option(y, y);
        }
    }
    topicSel.onchange = function() {
        //empty Chapters dropdown
        chapterSel.length = 1;
        //display correct values
        var z = subjectObject[subjectSel.value][this.value];
        for (var i = 0; i < z.length; i++) {
            chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
        }
    }
}
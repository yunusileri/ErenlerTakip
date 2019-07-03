function tarih_filtresi(value) {
    switch (value) {
        case "Bugün":
            window.location.replace("/devamsizlik/listele/Bugün/");
            break;
        case "Haftalık":
            window.location.replace("/devamsizlik/listele/Haftalık/");
            break;
        case "Aylık":
            window.location.replace("/devamsizlik/listele/Aylık/");
            break;
        case "Yıllık":
            window.location.replace("/devamsizlik/listele/Yıllık/");
            break;

    }
}

function zamanBelirle(uRl, t = "Bugün") {
    let index = -1;
    let tarih = "";
    let dizi = ["Y%C4%B1ll%C4%B1k", "Ayl%C4%B1k", "Haftal%C4%B1k", "Bug%C3%BCn"];
    for (let i = 0; i < 4; i++) {
        index = uRl.indexOf(dizi[i]);
        if (index !== -1) {
            switch (uRl[index]) {
                case "Y":
                    tarih = "Yıllık";
                    break;
                case "A":
                    tarih = "Aylık";
                    break;
                case "H":
                    tarih = "Haftalık";
                    break;
                case "B":
                    tarih = "Bugün";
                    break;
            }
            break;
        } else {
            tarih = t;
        }
    }
    return tarih;
}

function ders_filtresi(value) {
    let uRl = window.location.href;
    let tarih = zamanBelirle(uRl);
    window.location.replace("/devamsizlik/listele/" + tarih + "/" + value);
}


function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
    let input, filter, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    let div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("label");
    let txtValue;
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

function aClick(value) {
    let uRl = window.location.href;
    let ders = "";
    let tarih = zamanBelirle(uRl, "Yıllık");
    window.location.replace("/devamsizlik/listele/" + tarih + "/" + ders + "/" + value + "/");
}
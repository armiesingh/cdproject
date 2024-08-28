@echo off
for %%f in ("C:\Users\ZS135Bs\Desktop\ABDocking\Input\*.pdbqt") do (
    echo Processing ligand %%f
    mkdir "C:\Users\ZS135Bs\Desktop\ABDocking\Input\%%~nf"
    "C:\Users\ZS135Bs\Desktop\ABDocking\vina.exe" --config conf.txt --ligand "%%f" --out "C:\Users\ZS135Bs\Desktop\ABDocking\Input\%%~nf\out.pdbqt" --log "C:\Users\ZS135Bs\Desktop\ABDocking\Input\%%~nf\log.txt"
)

#!/usr/bin/env python
import gitlab
import os
import  requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

gl = gitlab.Gitlab.from_config("gitlab.gscorp.ad",["./.python-gitlab.cfg"])
#project_id = 1818
#project = gl.projects.get(project_id)

#raw = project.files.raw(file_path='build.gradle', ref='develop').decode("utf-8")
#print(raw)

def write_content_to_file(raw_content):
    if "org.apache.logging.log4j" in raw_content:
        with open("proyectos-log4j.csv", "a",encoding="utf-8") as libs:
            libs.write(f'{project.id},{project.name}')
            libs.write("\n")
    if "spv-commons-logging" in raw_content:
        with open("proyectos-spv-commons-logging.csv","a", encoding="utf-8") as libs:
            libs.write(f'{project.id},{project.name}')
            libs.write("\n")
    if "spv-commons-logger" in raw_content:
        with open("proyectos-spv-commons-logger.csv","a", encoding="utf-8") as libs:
            libs.write(f'{project.id},{project.name}')
            libs.write("\n")

def start():
    print("[+]Obteniendo proyectos")
    projects = gl.projects.list(all=True)
    print("[+] Listando proyectos")
    for project in projects:
        print(f'[+] Proyecto {project.id} {project.name}')
        try:
            print("[+] Obteniendo build.gradle")
            raw_content = project.files.raw(file_path='build.gradle', ref='develop').decode("utf-8")
            write_content_to_file(raw_content)
        except Exception as ex:
            try:
                print("[-] No tiene build.gradle")
                print("[+] Intentando pom.xml")
                raw_content = project.files.raw(file_path="pom.xml", ref='develop')
                write_content_to_file(raw_content)
            except Exception as ex:
                print("[-] No tiene pom.xml")


if __name__ == "__main__":
    start()

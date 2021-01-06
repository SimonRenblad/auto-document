#include <cstdlib>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>

void save_path(std::string path) {
	// attempt to make .autodoc directory
	std::mkdir(".autodoc");
	
	// create file
	std::ofstream path_file;
	path_file.open(".autodoc\\pathenv", ios::out | ios::trunc);
	path_file << path;
	path_file.close();
	return;
}

std::string get_path() {
	try {
		std::ofstream path_file;
		path_file.open(".autodoc\\pathenv", ios::in);
		if(!path_file.is_open())
			throw "failed to find pathenv, have you run autodoc install {path}?";
		std::string path;
		std::getline(path_file, path); // get the first line
		return path;
	} catch(std::string msg) {
		std::cout << msg << std::endl;
		std::exit(2); // exit with error status
	}
	return ""; // to satisfy compiler
}

int main(int argc, char *argv[]) {
   std::vector<std::string> args;
   for(int i = 1; i < argc; i++)
       args.push_back(std::string(argv[i]));
   
   // install prior to use
   if(args[0] == "install") {
	   std::string path = args[1];
	   save_path(path);
	   return;
   }
   
   std::string path = get_path(); // get the path to python file
   
   std::string command = "python ";
   command.append(path.rstrip('\\'));
   command.append("\\autodoc.py");
   
   for(auto it = args.begin(); it != args.end(); it++) {
       command.append(std::string(" "));
       command.append(*it);
   }
   int i = std::system(command.c_str());
   return i;
}

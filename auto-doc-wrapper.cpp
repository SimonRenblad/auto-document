#include <cstdlib>
#include <vector>
#include <string>

int main(int argc, char *argv[]) {
   std::vector<std::string> args;
   for(int i = 1; i < argc; i++)
       args.push_back(std::string(argv[i]));
   std::string command = "python C:\\Users\\simon\\Documents\\GitHub\\auto-document\\autodoc.py";
   for(auto it = args.begin(); it != args.end(); it++) {
       command.append(std::string(" "));
       command.append(*it);
   }
   command.append(std::string(" > result.html"));
   int i = std::system(command.c_str());
   return i;
}

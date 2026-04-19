#include "json.hpp"
#include <fstream>
#include <iostream>
#include <utility>

using nlohmann::json; //使用nlohmann命名空间下的json


json json_file_init(const auto &path) {
    std::ifstream f(path);
    /* 若文件不存在，则提示异常*/
    if (!f) {
        std::cerr << "文件打开异常" << std::endl;
        return "文件打开异常";
    };
    json data = json::parse(f);
    void close(); //关闭文件
    return data;
}

json json_merger(json file1, json file2) {
    json temp = std::move(file1); // 以file1作基础

    for (auto i = file2.begin(); i != file2.end(); ++i) {
        const std::string &key = i.key();
        auto &value = i.value();

        // 如果key已存在
        if (temp.find(key) != temp.end()) {
            auto &temp_value = temp[key]; //临时存储一个值
            //如果有嵌套，则只进行一次嵌套的合并
            if (temp_value.is_object() && value.is_object()) {
                for (auto j = value.begin(); j != value.end(); ++j) {
                    temp_value[j.key()] = j.value();
                }
            } else {
                //普通的key直接修改
                temp[key] = value;
            }
        } else {
            //新的key直接添加
            temp[key] = value;
        }
    }

    return temp;
}

int main() {
    std::string json_file_path[2] = {"", ""};

    //从用户输入获取json路径
    std::cout << "请输入原json路径（低优先级）：";
    std::cin >> json_file_path[0];
    std::cout << std::endl;
    std::cout << "请输入原json路径（高优先级）：";
    std::cin >> json_file_path[1];
    std::cout << std::endl;

    //合并文件
    json json_file1 = json_file_init(json_file_path[0]);
    json json_file2 = json_file_init(json_file_path[1]);
    json output = json_merger(json_file1, json_file2);

    //从用户输入获取输出路径
    std::string json_file_out_path;
    std::cout<<"请输入输出文件路径：";
    std::cin>>json_file_out_path;
    std::cout << std::endl;

    //写出文件
    std::ofstream outfile;
    outfile.open(json_file_out_path, std::ios::out | std::ios::trunc );
    outfile << output.dump(4)<<std::endl;
    void close();

};

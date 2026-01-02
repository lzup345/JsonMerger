#### 功能：合并两个json文件

## 使用方法
___
### 运行方法 I
1. **安装bext**`pip install bext`
2. **安装deepmerge**`pip install deepmerge`
3. **运行程序**`python main.py`
4. **根据提示输入**
### 运行方法 II
- **只提供x86_64**
- **Windows运行**`json_merger_windows.exe`
- **Linux中运行**`json_merger_linux`
    - Linux中需要确保文件具有可执行权限
---
### 如果为相对目录，那么实际操作文件路径为工作路径+相对路径
#### 例如：

#### 工作路径  
`~/tools/json_merger/`
#### 相对路径
`myfile.json`  
#### 那么则实际操作路径为
`~/tools/json_merger/myfile.json`

---
#### 最终文件输出在`./outputs/`中

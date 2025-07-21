# 🚀 ClassWidgets 统一构建工作流 (build_unified.yml)

这个工作流经过全面优化，将原来的多个构建工作流合并为一个高效、智能的统一构建流程。

## ✨ 触发方式

### 1. 标签推送 (Release 版本)
```bash
git tag v1.2.3
git push origin v1.2.3
```
- 触发条件：推送以 `v` 开头的标签
- 构建类型：**Release 版本**
- 包含签名：✅ (Windows)
- 自动发布：✅

### 2. 手动触发 (可选择 Release/Debug)
- 在 GitHub Actions 页面手动触发
- 可选择是否为发布版本
- 如果选择发布版本，需要提供版本号
- 构建类型：根据选择决定
- 包含签名：✅ (Release 版本的 Windows)

### 3. Pull Request (Debug 版本)
- 触发条件：创建或更新 PR
- 构建类型：**Debug 版本**
- 包含签名：❌
- 自动发布：❌

## 🏗️ 优化后的构建流程

### Job 1: Check (语法检查)
- **平台**: Windows, macOS, Ubuntu
- **功能**: 使用 `py_compile` 检查所有 Python 文件语法
- **失败处理**: 快速失败策略，语法检查失败立即终止整个构建流程
- **报告**: 错误信息写入 `GITHUB_STEP_SUMMARY`

### Job 2: Update-build-info (构建信息更新) 🆕
- **功能**: 独立设置构建信息，避免重复操作
- **优势**: 提高构建效率，统一管理构建元数据
- **输出**: 更新后的配置文件作为构建产物
- **信息包含**: 构建时间、提交哈希、分支、运行ID、构建类型等

### Job 3: Build (多平台构建)
- **依赖**: Check 和 Update-build-info 成功
- **Python 版本**: 3.8
- **构建工具**: 🔧 **统一使用 PyInstaller**（Linux 已优化）
- **平台支持**:
  - Windows x64/x86
  - macOS x64/arm64
  - Linux x64 (使用 PyInstaller 替代 Nuitka)
- **失败策略**: 快速失败，任何平台构建失败立即停止
- **优化**: 使用 `uv` 和缓存加速依赖安装

### Job 4: Sign (代码签名)
- **条件**: 仅在 Release 版本且构建成功时运行
- **平台**: 仅 Windows (x64/x86)
- **工具**: SignPath
- **流程**: 🚀 **简化签名流程** - 解压 → 直接签名 → 重新打包
- **优化**: 移除不必要的预压缩步骤

### Job 5: Package (智能打包) 🔥
- **依赖**: Build 成功，Sign 可选
- **优化亮点**:
  - 🚀 **缓存机制**: 使用 artifact_cache 优化文件查找
  - 🎯 **智能选择**: 优先使用签名版本，自动降级到构建版本
  - 📊 **性能提升**: 避免低效的 find 遍历
  - ❌ **错误处理**: 构建失败时不会尝试打包
- **输出**: 直接上传为 `ClassWidgets-Packages`
- **命名规范**:
  - **Debug 版本**: `ClassWidgets-{Platform}-{Arch}-Debug.zip`
  - **Release 版本**: `ClassWidgets-{Platform}-{Arch}.zip`

### Job 6: Upload-manifest (清单上传) 📋
- **功能**: 生成详细的构建清单文档
- **优化**: 🆕 **使用 `actions/upload-artifact@v4.4.2` 直接上传**
- **产物**: `ClassWidgets-Manifest` 构建产物
- **内容**: 构建信息、文件详情、MD5 校验等
- **输出**: 同时更新 `GITHUB_STEP_SUMMARY`

### Job 7: Release (发布版本)
- **条件**: 仅在 Release 版本且打包成功时运行
- **依赖**: Package 成功
- **功能**: 调用 `release.yml` 进行版本发布

## 🔧 构建信息

每个构建都会在 `config/default_config.json` 中写入以下信息：
- **构建时间** (UTC+8)
- **提交哈希** (前7位)
- **分支名称**
- **运行ID**
- **构建类型** (release/debug)
- **是否发布版本**

## 📦 GitHub Artifacts (优化命名)

### 🎯 **统一命名规范**
- **ClassWidgets-Packages**: 最终打包的所有平台文件
- **ClassWidgets-Manifest**: 构建清单文档
- **各平台构建产物**: `{platform}-{arch}-build`
- **Windows签名产物**: `windows-{arch}-signed` (仅发布版本)

### 🏷️ **文件命名**
- **Debug 版本**: `ClassWidgets-{Platform}-{Arch}-Debug.zip`
- **Release 版本**: `ClassWidgets-{Platform}-{Arch}.zip`

## 🚀 优化改进亮点

### ⚡ **性能优化**
1. **缓存机制**: 使用 artifact_cache 大幅提升文件查找效率
2. **快速失败**: 构建失败立即停止，避免资源浪费
3. **统一工具**: Linux 改用 PyInstaller，简化构建流程
4. **独立Job**: 构建信息设置提取为独立 job，避免重复操作

### 📦 **打包优化**
1. **简化签名**: 直接签名流程，移除不必要的预压缩
2. **统一命名**: 规范 artifact 命名规则，避免混乱
3. **智能选择**: 优先使用签名版本，自动降级机制
4. **直接上传**: 使用 `actions/upload-artifact` 直接上传清单

### 🛡️ **错误处理**
1. **构建失败检测**: 构建失败时不会尝试打包
2. **文件验证**: 确保所有必需文件存在
3. **详细日志**: 提供清晰的错误信息和状态反馈
4. **快速失败**: 任何关键步骤失败都会立即停止工作流

## 🎯 主要优势

1. **🔄 统一管理**: 一个工作流管理所有平台构建
2. **🧠 智能触发**: 根据触发方式自动判断构建类型
3. **⚙️ 灵活配置**: 支持手动选择发布/调试模式
4. **📈 性能提升**: 缓存机制和优化算法大幅提升构建速度
5. **📊 详细报告**: 丰富的构建信息和错误报告
6. **🚀 快速失败**: 避免无效构建，节省资源和时间
7. **🔧 简化维护**: 统一工具链，降低维护复杂度

## 🚨 注意事项

- ✅ 确保 `requirements.txt` 文件存在且正确
- 🔐 Windows 签名需要配置 `SIGNPATH_API_TOKEN` 密钥
- 🐧 Linux 构建已优化为使用 PyInstaller
- 📋 发布功能依赖于 `release.yml` 工作流的存在
- ⚡ 快速失败策略：任何步骤失败都会立即停止工作流
- 💾 构建产物会占用 GitHub Actions 存储空间

## 🔍 故障排除

- **构建失败**: 检查 Check job 的输出，通常是语法或依赖问题
- **签名失败**: 验证 SignPath 配置和 API Token
- **发布失败**: 确保标签格式正确（v开头的语义化版本）
- **打包失败**: 检查是否有构建产物生成，确认构建步骤成功
- **平台特定问题**: 查看对应平台的构建日志

---

*这个全面优化的统一工作流让构建过程更加高效、智能和可靠！杳杳可以放心使用~ (｡◕‿◕｡)* ✨
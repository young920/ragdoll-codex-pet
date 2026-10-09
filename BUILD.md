# 构建记录

## 1. 角色形象

从 `archive/v1/source/front.png` 的布偶猫正面形象确定颜色和脸部特征。第一版图集在 `archive/v1/`，主要靠基础姿势的变形来表现动作，因此变化较少。

第二版继续使用同一基础形象，生成了独立的待机、左右移动、挥手、跳跃、失败、等待、工作和检查动作条。原图放在 `process/decoded/`，对应提示词放在 `process/prompts/rows/`。

## 2. 标准动作

`process/pet_request.json` 记录了图集布局和帧数；`process/imagegen-jobs.json` 是生成前的任务计划，因此其中的初始 `pending` 状态不是完成状态。每个动作条经过逐帧提取和检查，检查报告位于 `process/qa/rows/`。九种动作合成后形成 `process/qa/standard-atlas.png`。

跳跃动作的最高帧比落点高 41 像素，最后一帧回到待机基线。挥手使用与身体相连的前爪；工作状态使用专注思考和抬爪姿势。

## 3. 视线方向

先生成上、右、下、左四个锚点，再生成顺时针的两个八帧方向条。第一次右半圈方向条间距过小，未通过帧分离检查；保存在 `process/decoded/look-row-9.png`。修订版 `look-row-9-revision.png` 通过注册检查，并与 `look-row-10.png` 合成完整十六方向。

## 4. 边缘清理与质量门槛

洋红色背景在合成后进行了一次边缘去色，生成最终的 `spritesheet.png`。保留的报告包括：

- `process/final/validation-extended.json`：图集结构、透明度、色边和内容检查。
- `process/qa/chroma-despill-extended.json`：边缘去色记录。
- `process/qa/standard-review.json`：九种动作的逐帧检查。
- `process/qa/look-continuity.json` 与 `direction-semantics.json`：方向连续性和人工方向判读。
- `process/qa/pet-quality.json`：最终综合质量检查。

最终检查 `ok: true`，但记录了两条人工复核提示：朝上帧耳朵之间的透明间隙被几何检查标记，以及 270° 到 292.5° 的帧差大于邻近帧。接触表上未见角色断裂或方向反转。

## 5. 预览和安装包

`process/render_final_previews.py` 从最终编码图集裁出预览帧；因此预览与发布图集对应。仓库根目录的两个文件就是安装包。`process/` 中的工作流元数据和报告已把本机绝对路径改为仓库相对路径。

使用到的图集提取、合成和验证脚本来自 Pets 工作流，未复制进本仓库；`process/prompts/`、源图、逐帧产物和报告完整保存了这次制作的输入与结果。

       �K"	  ����Abrain.Event:2�ɟ�Y      �d��	������A"��
a
inputs/x_inputsPlaceholder*
dtype0*
shape: *'
_output_shapes
:���������
a
inputs/y_inputsPlaceholder*
dtype0*
shape: *'
_output_shapes
:���������
r
!layer/weights/random_normal/shapeConst*
dtype0*
valueB"   
   *
_output_shapes
:
e
 layer/weights/random_normal/meanConst*
dtype0*
valueB
 *    *
_output_shapes
: 
g
"layer/weights/random_normal/stddevConst*
dtype0*
valueB
 *  �?*
_output_shapes
: 
�
0layer/weights/random_normal/RandomStandardNormalRandomStandardNormal!layer/weights/random_normal/shape*
dtype0*
seed2 *

seed *
T0*
_output_shapes

:

�
layer/weights/random_normal/mulMul0layer/weights/random_normal/RandomStandardNormal"layer/weights/random_normal/stddev*
T0*
_output_shapes

:

�
layer/weights/random_normalAddlayer/weights/random_normal/mul layer/weights/random_normal/mean*
T0*
_output_shapes

:

�
layer/weights/WVariable*
dtype0*
shape
:
*
	container *
shared_name *
_output_shapes

:

�
layer/weights/W/AssignAssignlayer/weights/Wlayer/weights/random_normal*
validate_shape(*"
_class
loc:@layer/weights/W*
use_locking(*
T0*
_output_shapes

:

~
layer/weights/W/readIdentitylayer/weights/W*"
_class
loc:@layer/weights/W*
T0*
_output_shapes

:

g
layer/biases/zerosConst*
dtype0*
valueB
*    *
_output_shapes

:

W
layer/biases/add/yConst*
dtype0*
valueB
 *���=*
_output_shapes
: 
h
layer/biases/addAddlayer/biases/zeroslayer/biases/add/y*
T0*
_output_shapes

:

�
layer/biases/bVariable*
dtype0*
shape
:
*
	container *
shared_name *
_output_shapes

:

�
layer/biases/b/AssignAssignlayer/biases/blayer/biases/add*
validate_shape(*!
_class
loc:@layer/biases/b*
use_locking(*
T0*
_output_shapes

:

{
layer/biases/b/readIdentitylayer/biases/b*!
_class
loc:@layer/biases/b*
T0*
_output_shapes

:

�
layer/Wx_plus_b/MatMulMatMulinputs/x_inputslayer/weights/W/read*
transpose_b( *
transpose_a( *
T0*'
_output_shapes
:���������

y
layer/Wx_plus_b/AddAddlayer/Wx_plus_b/MatMullayer/biases/b/read*
T0*'
_output_shapes
:���������

Y

layer/ReluRelulayer/Wx_plus_b/Add*
T0*'
_output_shapes
:���������

t
#layer_1/weights/random_normal/shapeConst*
dtype0*
valueB"
      *
_output_shapes
:
g
"layer_1/weights/random_normal/meanConst*
dtype0*
valueB
 *    *
_output_shapes
: 
i
$layer_1/weights/random_normal/stddevConst*
dtype0*
valueB
 *  �?*
_output_shapes
: 
�
2layer_1/weights/random_normal/RandomStandardNormalRandomStandardNormal#layer_1/weights/random_normal/shape*
dtype0*
seed2 *

seed *
T0*
_output_shapes

:

�
!layer_1/weights/random_normal/mulMul2layer_1/weights/random_normal/RandomStandardNormal$layer_1/weights/random_normal/stddev*
T0*
_output_shapes

:

�
layer_1/weights/random_normalAdd!layer_1/weights/random_normal/mul"layer_1/weights/random_normal/mean*
T0*
_output_shapes

:

�
layer_1/weights/WVariable*
dtype0*
shape
:
*
	container *
shared_name *
_output_shapes

:

�
layer_1/weights/W/AssignAssignlayer_1/weights/Wlayer_1/weights/random_normal*
validate_shape(*$
_class
loc:@layer_1/weights/W*
use_locking(*
T0*
_output_shapes

:

�
layer_1/weights/W/readIdentitylayer_1/weights/W*$
_class
loc:@layer_1/weights/W*
T0*
_output_shapes

:

i
layer_1/biases/zerosConst*
dtype0*
valueB*    *
_output_shapes

:
Y
layer_1/biases/add/yConst*
dtype0*
valueB
 *���=*
_output_shapes
: 
n
layer_1/biases/addAddlayer_1/biases/zeroslayer_1/biases/add/y*
T0*
_output_shapes

:
�
layer_1/biases/bVariable*
dtype0*
shape
:*
	container *
shared_name *
_output_shapes

:
�
layer_1/biases/b/AssignAssignlayer_1/biases/blayer_1/biases/add*
validate_shape(*#
_class
loc:@layer_1/biases/b*
use_locking(*
T0*
_output_shapes

:
�
layer_1/biases/b/readIdentitylayer_1/biases/b*#
_class
loc:@layer_1/biases/b*
T0*
_output_shapes

:
�
layer_1/Wx_plus_b/MatMulMatMul
layer/Relulayer_1/weights/W/read*
transpose_b( *
transpose_a( *
T0*'
_output_shapes
:���������

layer_1/Wx_plus_b/AddAddlayer_1/Wx_plus_b/MatMullayer_1/biases/b/read*
T0*'
_output_shapes
:���������
i
loss/subSubinputs/y_inputslayer_1/Wx_plus_b/Add*
T0*'
_output_shapes
:���������
Q
loss/SquareSquareloss/sub*
T0*'
_output_shapes
:���������
d
loss/Sum/reduction_indicesConst*
dtype0*
valueB:*
_output_shapes
:
w
loss/SumSumloss/Squareloss/Sum/reduction_indices*
T0*
	keep_dims( *#
_output_shapes
:���������
<
	loss/RankRankloss/Sum*
T0*
_output_shapes
: 
R
loss/range/startConst*
dtype0*
value	B : *
_output_shapes
: 
R
loss/range/deltaConst*
dtype0*
value	B :*
_output_shapes
: 
^

loss/rangeRangeloss/range/start	loss/Rankloss/range/delta*
_output_shapes
:
Y
	loss/MeanMeanloss/Sum
loss/range*
T0*
	keep_dims( *
_output_shapes
: 
L
train/gradients/ShapeShape	loss/Mean*
T0*
_output_shapes
: 
Z
train/gradients/ConstConst*
dtype0*
valueB
 *  �?*
_output_shapes
: 
k
train/gradients/FillFilltrain/gradients/Shapetrain/gradients/Const*
T0*
_output_shapes
: 
\
$train/gradients/loss/Mean_grad/ShapeShapeloss/Sum*
T0*
_output_shapes
:
V
#train/gradients/loss/Mean_grad/RankRankloss/Sum*
T0*
_output_shapes
: 
`
&train/gradients/loss/Mean_grad/Shape_1Shape
loss/range*
T0*
_output_shapes
:
l
*train/gradients/loss/Mean_grad/range/startConst*
dtype0*
value	B : *
_output_shapes
: 
l
*train/gradients/loss/Mean_grad/range/deltaConst*
dtype0*
value	B :*
_output_shapes
: 
�
$train/gradients/loss/Mean_grad/rangeRange*train/gradients/loss/Mean_grad/range/start#train/gradients/loss/Mean_grad/Rank*train/gradients/loss/Mean_grad/range/delta*
_output_shapes
:
k
)train/gradients/loss/Mean_grad/Fill/valueConst*
dtype0*
value	B :*
_output_shapes
: 
�
#train/gradients/loss/Mean_grad/FillFill&train/gradients/loss/Mean_grad/Shape_1)train/gradients/loss/Mean_grad/Fill/value*
T0*
_output_shapes
:
�
,train/gradients/loss/Mean_grad/DynamicStitchDynamicStitch$train/gradients/loss/Mean_grad/range
loss/range$train/gradients/loss/Mean_grad/Shape#train/gradients/loss/Mean_grad/Fill*#
_output_shapes
:���������*
T0*
N
�
'train/gradients/loss/Mean_grad/floordivDiv$train/gradients/loss/Mean_grad/Shape,train/gradients/loss/Mean_grad/DynamicStitch*
T0*#
_output_shapes
:���������
�
&train/gradients/loss/Mean_grad/ReshapeReshapetrain/gradients/Fill,train/gradients/loss/Mean_grad/DynamicStitch*
T0*
_output_shapes
:
�
#train/gradients/loss/Mean_grad/TileTile&train/gradients/loss/Mean_grad/Reshape'train/gradients/loss/Mean_grad/floordiv*
T0*
_output_shapes
:
^
&train/gradients/loss/Mean_grad/Shape_2Shapeloss/Sum*
T0*
_output_shapes
:
]
&train/gradients/loss/Mean_grad/Shape_3Shape	loss/Mean*
T0*
_output_shapes
: 
v
%train/gradients/loss/Mean_grad/Rank_1Rank&train/gradients/loss/Mean_grad/Shape_2*
T0*
_output_shapes
: 
n
,train/gradients/loss/Mean_grad/range_1/startConst*
dtype0*
value	B : *
_output_shapes
: 
n
,train/gradients/loss/Mean_grad/range_1/deltaConst*
dtype0*
value	B :*
_output_shapes
: 
�
&train/gradients/loss/Mean_grad/range_1Range,train/gradients/loss/Mean_grad/range_1/start%train/gradients/loss/Mean_grad/Rank_1,train/gradients/loss/Mean_grad/range_1/delta*
_output_shapes
:
�
#train/gradients/loss/Mean_grad/ProdProd&train/gradients/loss/Mean_grad/Shape_2&train/gradients/loss/Mean_grad/range_1*
T0*
	keep_dims( *
_output_shapes
: 
v
%train/gradients/loss/Mean_grad/Rank_2Rank&train/gradients/loss/Mean_grad/Shape_3*
T0*
_output_shapes
: 
n
,train/gradients/loss/Mean_grad/range_2/startConst*
dtype0*
value	B : *
_output_shapes
: 
n
,train/gradients/loss/Mean_grad/range_2/deltaConst*
dtype0*
value	B :*
_output_shapes
: 
�
&train/gradients/loss/Mean_grad/range_2Range,train/gradients/loss/Mean_grad/range_2/start%train/gradients/loss/Mean_grad/Rank_2,train/gradients/loss/Mean_grad/range_2/delta*
_output_shapes
:
�
%train/gradients/loss/Mean_grad/Prod_1Prod&train/gradients/loss/Mean_grad/Shape_3&train/gradients/loss/Mean_grad/range_2*
T0*
	keep_dims( *
_output_shapes
: 
�
)train/gradients/loss/Mean_grad/floordiv_1Div#train/gradients/loss/Mean_grad/Prod%train/gradients/loss/Mean_grad/Prod_1*
T0*
_output_shapes
: 
�
#train/gradients/loss/Mean_grad/CastCast)train/gradients/loss/Mean_grad/floordiv_1*

DstT0*

SrcT0*
_output_shapes
: 
�
&train/gradients/loss/Mean_grad/truedivDiv#train/gradients/loss/Mean_grad/Tile#train/gradients/loss/Mean_grad/Cast*
T0*
_output_shapes
:
^
#train/gradients/loss/Sum_grad/ShapeShapeloss/Square*
T0*
_output_shapes
:
X
"train/gradients/loss/Sum_grad/RankRankloss/Square*
T0*
_output_shapes
: 
o
%train/gradients/loss/Sum_grad/Shape_1Shapeloss/Sum/reduction_indices*
T0*
_output_shapes
:
k
)train/gradients/loss/Sum_grad/range/startConst*
dtype0*
value	B : *
_output_shapes
: 
k
)train/gradients/loss/Sum_grad/range/deltaConst*
dtype0*
value	B :*
_output_shapes
: 
�
#train/gradients/loss/Sum_grad/rangeRange)train/gradients/loss/Sum_grad/range/start"train/gradients/loss/Sum_grad/Rank)train/gradients/loss/Sum_grad/range/delta*
_output_shapes
:
j
(train/gradients/loss/Sum_grad/Fill/valueConst*
dtype0*
value	B :*
_output_shapes
: 
�
"train/gradients/loss/Sum_grad/FillFill%train/gradients/loss/Sum_grad/Shape_1(train/gradients/loss/Sum_grad/Fill/value*
T0*
_output_shapes
:
�
+train/gradients/loss/Sum_grad/DynamicStitchDynamicStitch#train/gradients/loss/Sum_grad/rangeloss/Sum/reduction_indices#train/gradients/loss/Sum_grad/Shape"train/gradients/loss/Sum_grad/Fill*#
_output_shapes
:���������*
T0*
N
�
&train/gradients/loss/Sum_grad/floordivDiv#train/gradients/loss/Sum_grad/Shape+train/gradients/loss/Sum_grad/DynamicStitch*
T0*
_output_shapes
:
�
%train/gradients/loss/Sum_grad/ReshapeReshape&train/gradients/loss/Mean_grad/truediv+train/gradients/loss/Sum_grad/DynamicStitch*
T0*
_output_shapes
:
�
"train/gradients/loss/Sum_grad/TileTile%train/gradients/loss/Sum_grad/Reshape&train/gradients/loss/Sum_grad/floordiv*
T0*0
_output_shapes
:������������������
�
&train/gradients/loss/Square_grad/mul/xConst#^train/gradients/loss/Sum_grad/Tile*
dtype0*
valueB
 *   @*
_output_shapes
: 
�
$train/gradients/loss/Square_grad/mulMul&train/gradients/loss/Square_grad/mul/xloss/sub*
T0*'
_output_shapes
:���������
�
&train/gradients/loss/Square_grad/mul_1Mul"train/gradients/loss/Sum_grad/Tile$train/gradients/loss/Square_grad/mul*
T0*0
_output_shapes
:������������������
b
#train/gradients/loss/sub_grad/ShapeShapeinputs/y_inputs*
T0*
_output_shapes
:
j
%train/gradients/loss/sub_grad/Shape_1Shapelayer_1/Wx_plus_b/Add*
T0*
_output_shapes
:
�
3train/gradients/loss/sub_grad/BroadcastGradientArgsBroadcastGradientArgs#train/gradients/loss/sub_grad/Shape%train/gradients/loss/sub_grad/Shape_1*2
_output_shapes 
:���������:���������
�
!train/gradients/loss/sub_grad/SumSum&train/gradients/loss/Square_grad/mul_13train/gradients/loss/sub_grad/BroadcastGradientArgs*
T0*
	keep_dims( *
_output_shapes
:
�
%train/gradients/loss/sub_grad/ReshapeReshape!train/gradients/loss/sub_grad/Sum#train/gradients/loss/sub_grad/Shape*
T0*0
_output_shapes
:������������������
�
#train/gradients/loss/sub_grad/Sum_1Sum&train/gradients/loss/Square_grad/mul_15train/gradients/loss/sub_grad/BroadcastGradientArgs:1*
T0*
	keep_dims( *
_output_shapes
:
p
!train/gradients/loss/sub_grad/NegNeg#train/gradients/loss/sub_grad/Sum_1*
T0*
_output_shapes
:
�
'train/gradients/loss/sub_grad/Reshape_1Reshape!train/gradients/loss/sub_grad/Neg%train/gradients/loss/sub_grad/Shape_1*
T0*0
_output_shapes
:������������������
�
.train/gradients/loss/sub_grad/tuple/group_depsNoOp&^train/gradients/loss/sub_grad/Reshape(^train/gradients/loss/sub_grad/Reshape_1
�
6train/gradients/loss/sub_grad/tuple/control_dependencyIdentity%train/gradients/loss/sub_grad/Reshape/^train/gradients/loss/sub_grad/tuple/group_deps*8
_class.
,*loc:@train/gradients/loss/sub_grad/Reshape*
T0*0
_output_shapes
:������������������
�
8train/gradients/loss/sub_grad/tuple/control_dependency_1Identity'train/gradients/loss/sub_grad/Reshape_1/^train/gradients/loss/sub_grad/tuple/group_deps*:
_class0
.,loc:@train/gradients/loss/sub_grad/Reshape_1*
T0*0
_output_shapes
:������������������
x
0train/gradients/layer_1/Wx_plus_b/Add_grad/ShapeShapelayer_1/Wx_plus_b/MatMul*
T0*
_output_shapes
:
w
2train/gradients/layer_1/Wx_plus_b/Add_grad/Shape_1Shapelayer_1/biases/b/read*
T0*
_output_shapes
:
�
@train/gradients/layer_1/Wx_plus_b/Add_grad/BroadcastGradientArgsBroadcastGradientArgs0train/gradients/layer_1/Wx_plus_b/Add_grad/Shape2train/gradients/layer_1/Wx_plus_b/Add_grad/Shape_1*2
_output_shapes 
:���������:���������
�
.train/gradients/layer_1/Wx_plus_b/Add_grad/SumSum8train/gradients/loss/sub_grad/tuple/control_dependency_1@train/gradients/layer_1/Wx_plus_b/Add_grad/BroadcastGradientArgs*
T0*
	keep_dims( *
_output_shapes
:
�
2train/gradients/layer_1/Wx_plus_b/Add_grad/ReshapeReshape.train/gradients/layer_1/Wx_plus_b/Add_grad/Sum0train/gradients/layer_1/Wx_plus_b/Add_grad/Shape*
T0*0
_output_shapes
:������������������
�
0train/gradients/layer_1/Wx_plus_b/Add_grad/Sum_1Sum8train/gradients/loss/sub_grad/tuple/control_dependency_1Btrain/gradients/layer_1/Wx_plus_b/Add_grad/BroadcastGradientArgs:1*
T0*
	keep_dims( *
_output_shapes
:
�
4train/gradients/layer_1/Wx_plus_b/Add_grad/Reshape_1Reshape0train/gradients/layer_1/Wx_plus_b/Add_grad/Sum_12train/gradients/layer_1/Wx_plus_b/Add_grad/Shape_1*
T0*
_output_shapes

:
�
;train/gradients/layer_1/Wx_plus_b/Add_grad/tuple/group_depsNoOp3^train/gradients/layer_1/Wx_plus_b/Add_grad/Reshape5^train/gradients/layer_1/Wx_plus_b/Add_grad/Reshape_1
�
Ctrain/gradients/layer_1/Wx_plus_b/Add_grad/tuple/control_dependencyIdentity2train/gradients/layer_1/Wx_plus_b/Add_grad/Reshape<^train/gradients/layer_1/Wx_plus_b/Add_grad/tuple/group_deps*E
_class;
97loc:@train/gradients/layer_1/Wx_plus_b/Add_grad/Reshape*
T0*0
_output_shapes
:������������������
�
Etrain/gradients/layer_1/Wx_plus_b/Add_grad/tuple/control_dependency_1Identity4train/gradients/layer_1/Wx_plus_b/Add_grad/Reshape_1<^train/gradients/layer_1/Wx_plus_b/Add_grad/tuple/group_deps*G
_class=
;9loc:@train/gradients/layer_1/Wx_plus_b/Add_grad/Reshape_1*
T0*
_output_shapes

:
�
4train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMulMatMulCtrain/gradients/layer_1/Wx_plus_b/Add_grad/tuple/control_dependencylayer_1/weights/W/read*
transpose_b(*
transpose_a( *
T0*'
_output_shapes
:���������

�
6train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMul_1MatMul
layer/ReluCtrain/gradients/layer_1/Wx_plus_b/Add_grad/tuple/control_dependency*
transpose_b( *
transpose_a(*
T0*'
_output_shapes
:
���������
�
>train/gradients/layer_1/Wx_plus_b/MatMul_grad/tuple/group_depsNoOp5^train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMul7^train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMul_1
�
Ftrain/gradients/layer_1/Wx_plus_b/MatMul_grad/tuple/control_dependencyIdentity4train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMul?^train/gradients/layer_1/Wx_plus_b/MatMul_grad/tuple/group_deps*G
_class=
;9loc:@train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMul*
T0*'
_output_shapes
:���������

�
Htrain/gradients/layer_1/Wx_plus_b/MatMul_grad/tuple/control_dependency_1Identity6train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMul_1?^train/gradients/layer_1/Wx_plus_b/MatMul_grad/tuple/group_deps*I
_class?
=;loc:@train/gradients/layer_1/Wx_plus_b/MatMul_grad/MatMul_1*
T0*'
_output_shapes
:
���������
�
(train/gradients/layer/Relu_grad/ReluGradReluGradFtrain/gradients/layer_1/Wx_plus_b/MatMul_grad/tuple/control_dependency
layer/Relu*
T0*'
_output_shapes
:���������

t
.train/gradients/layer/Wx_plus_b/Add_grad/ShapeShapelayer/Wx_plus_b/MatMul*
T0*
_output_shapes
:
s
0train/gradients/layer/Wx_plus_b/Add_grad/Shape_1Shapelayer/biases/b/read*
T0*
_output_shapes
:
�
>train/gradients/layer/Wx_plus_b/Add_grad/BroadcastGradientArgsBroadcastGradientArgs.train/gradients/layer/Wx_plus_b/Add_grad/Shape0train/gradients/layer/Wx_plus_b/Add_grad/Shape_1*2
_output_shapes 
:���������:���������
�
,train/gradients/layer/Wx_plus_b/Add_grad/SumSum(train/gradients/layer/Relu_grad/ReluGrad>train/gradients/layer/Wx_plus_b/Add_grad/BroadcastGradientArgs*
T0*
	keep_dims( *
_output_shapes
:
�
0train/gradients/layer/Wx_plus_b/Add_grad/ReshapeReshape,train/gradients/layer/Wx_plus_b/Add_grad/Sum.train/gradients/layer/Wx_plus_b/Add_grad/Shape*
T0*0
_output_shapes
:������������������
�
.train/gradients/layer/Wx_plus_b/Add_grad/Sum_1Sum(train/gradients/layer/Relu_grad/ReluGrad@train/gradients/layer/Wx_plus_b/Add_grad/BroadcastGradientArgs:1*
T0*
	keep_dims( *
_output_shapes
:
�
2train/gradients/layer/Wx_plus_b/Add_grad/Reshape_1Reshape.train/gradients/layer/Wx_plus_b/Add_grad/Sum_10train/gradients/layer/Wx_plus_b/Add_grad/Shape_1*
T0*
_output_shapes

:

�
9train/gradients/layer/Wx_plus_b/Add_grad/tuple/group_depsNoOp1^train/gradients/layer/Wx_plus_b/Add_grad/Reshape3^train/gradients/layer/Wx_plus_b/Add_grad/Reshape_1
�
Atrain/gradients/layer/Wx_plus_b/Add_grad/tuple/control_dependencyIdentity0train/gradients/layer/Wx_plus_b/Add_grad/Reshape:^train/gradients/layer/Wx_plus_b/Add_grad/tuple/group_deps*C
_class9
75loc:@train/gradients/layer/Wx_plus_b/Add_grad/Reshape*
T0*0
_output_shapes
:������������������
�
Ctrain/gradients/layer/Wx_plus_b/Add_grad/tuple/control_dependency_1Identity2train/gradients/layer/Wx_plus_b/Add_grad/Reshape_1:^train/gradients/layer/Wx_plus_b/Add_grad/tuple/group_deps*E
_class;
97loc:@train/gradients/layer/Wx_plus_b/Add_grad/Reshape_1*
T0*
_output_shapes

:

�
2train/gradients/layer/Wx_plus_b/MatMul_grad/MatMulMatMulAtrain/gradients/layer/Wx_plus_b/Add_grad/tuple/control_dependencylayer/weights/W/read*
transpose_b(*
transpose_a( *
T0*'
_output_shapes
:���������
�
4train/gradients/layer/Wx_plus_b/MatMul_grad/MatMul_1MatMulinputs/x_inputsAtrain/gradients/layer/Wx_plus_b/Add_grad/tuple/control_dependency*
transpose_b( *
transpose_a(*
T0*'
_output_shapes
:���������
�
<train/gradients/layer/Wx_plus_b/MatMul_grad/tuple/group_depsNoOp3^train/gradients/layer/Wx_plus_b/MatMul_grad/MatMul5^train/gradients/layer/Wx_plus_b/MatMul_grad/MatMul_1
�
Dtrain/gradients/layer/Wx_plus_b/MatMul_grad/tuple/control_dependencyIdentity2train/gradients/layer/Wx_plus_b/MatMul_grad/MatMul=^train/gradients/layer/Wx_plus_b/MatMul_grad/tuple/group_deps*E
_class;
97loc:@train/gradients/layer/Wx_plus_b/MatMul_grad/MatMul*
T0*'
_output_shapes
:���������
�
Ftrain/gradients/layer/Wx_plus_b/MatMul_grad/tuple/control_dependency_1Identity4train/gradients/layer/Wx_plus_b/MatMul_grad/MatMul_1=^train/gradients/layer/Wx_plus_b/MatMul_grad/tuple/group_deps*G
_class=
;9loc:@train/gradients/layer/Wx_plus_b/MatMul_grad/MatMul_1*
T0*'
_output_shapes
:���������
h
#train/GradientDescent/learning_rateConst*
dtype0*
valueB
 *���=*
_output_shapes
: 
�
Atrain/GradientDescent/update_layer/weights/W/ApplyGradientDescentApplyGradientDescentlayer/weights/W#train/GradientDescent/learning_rateFtrain/gradients/layer/Wx_plus_b/MatMul_grad/tuple/control_dependency_1*"
_class
loc:@layer/weights/W*
use_locking( *
T0*
_output_shapes

:

�
@train/GradientDescent/update_layer/biases/b/ApplyGradientDescentApplyGradientDescentlayer/biases/b#train/GradientDescent/learning_rateCtrain/gradients/layer/Wx_plus_b/Add_grad/tuple/control_dependency_1*!
_class
loc:@layer/biases/b*
use_locking( *
T0*
_output_shapes

:

�
Ctrain/GradientDescent/update_layer_1/weights/W/ApplyGradientDescentApplyGradientDescentlayer_1/weights/W#train/GradientDescent/learning_rateHtrain/gradients/layer_1/Wx_plus_b/MatMul_grad/tuple/control_dependency_1*$
_class
loc:@layer_1/weights/W*
use_locking( *
T0*
_output_shapes

:

�
Btrain/GradientDescent/update_layer_1/biases/b/ApplyGradientDescentApplyGradientDescentlayer_1/biases/b#train/GradientDescent/learning_rateEtrain/gradients/layer_1/Wx_plus_b/Add_grad/tuple/control_dependency_1*#
_class
loc:@layer_1/biases/b*
use_locking( *
T0*
_output_shapes

:
�
train/GradientDescentNoOpB^train/GradientDescent/update_layer/weights/W/ApplyGradientDescentA^train/GradientDescent/update_layer/biases/b/ApplyGradientDescentD^train/GradientDescent/update_layer_1/weights/W/ApplyGradientDescentC^train/GradientDescent/update_layer_1/biases/b/ApplyGradientDescent"	GU	�
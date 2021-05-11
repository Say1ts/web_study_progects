<?php

use yii\helpers\Html;
use yii\grid\GridView;

/* @var $this yii\web\View */
/* @var $dataProvider yii\data\ActiveDataProvider */
/* @var $model app\models\PdfFile */

$this->title = 'Список загруженных документов';
$this->params['breadcrumbs'][] = $this->title;
?>
<div class="pdf-file-index">

    <h1><?= Html::encode($this->title) ?></h1>

    <p>
        <?= Html::a('Добавить документ', ['create'], ['class' => 'btn btn-success']) ?>
    </p>


    <?= GridView::widget([
        'dataProvider' => $dataProvider,
        'columns' => [
            ['class' => 'yii\grid\SerialColumn'],

            'title',
            'content',
            'file',

            ['class' => 'yii\grid\ActionColumn'],
        ],
    ]); ?>


</div>

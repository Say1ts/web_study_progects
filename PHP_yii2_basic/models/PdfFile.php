<?php

namespace app\models;

use Yii;

/**
 * This is the model class for table "pdffiles".
 *
 * @property int $id
 * @property string $title
 * @property string $content
 * @property string $file
 */
class PdfFile extends \yii\db\ActiveRecord
{
    /**
     * {@inheritdoc}
     */
    public static function tableName()
    {
        return 'pdffiles';
    }

    /**
     * {@inheritdoc}
     */
    public function rules()
    {
        return [
            [['title', 'content', 'file'], 'required'],
            [['title', 'file'], 'string', 'max' => 100],
            [['content'], 'string', 'max' => 250],
        ];
    }

    /**
     * {@inheritdoc}
     */
    public function attributeLabels()
    {
        return [
            'id' => 'ID',
            'title' => 'Title',
            'content' => 'Content',
            'file' => 'File',
        ];
    }
}

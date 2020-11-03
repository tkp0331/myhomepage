from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="カテゴリ名", max_length=255)
    slug = models.SlugField(verbose_name="スラッグ", unique=True)

    def __str__(self):
        """
        各カテゴリ毎に格納されている値を返す。
        ex) name = "プログラミング" であったら"プログラミング"
        これを指定することで、一覧表示などの際にカテゴリ名が表示される。
        区別ができる文字列を返すようすると良い。
        """
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name="タグ名", max_length=255)
    slug = models.SlugField(verbose_name="スラッグ", unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=255)
    subtitle = models.CharField(
        verbose_name="サブタイトル", max_length=255, blank=True, null=True)
    # ForeignKeyフィールドは1対多の関係を表す
    # この場合は1つのカテゴリに対して複数のブログが紐づく
    # blank=Trueを指定すると、何も指定しないことを許す
    category = models.ForeignKey(
        Category, verbose_name="カテゴリ", on_delete=models.DO_NOTHING, blank=True)
    # ManyToManyFieldは多対多の関係を表す
    tags = models.ManyToManyField(Tag, verbose_name="タグ", blank=True)
    content = models.TextField(verbose_name="本文", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blog"
        # レコード取得時に降順（＝新しい順）にソートして返す
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

from io import BytesIO

import requests
from django.core import files
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from app.forms import AddImageForm, ChangeSizeForm
from app.models import Image
from PIL import Image as ImagePIL


class HomePageView(ListView):
    """ Представление для всех изображений"""

    model = Image
    template_name = 'app/index.html'
    context_object_name = 'images'

    def get_queryset(self):
        """
        Queryset всех изображений
        Returns:
            Image.objects.all()
        """
        return Image.objects.all()


def image_details_view(request, image_id):
    """
    Представление для изображения и изменения его размеров
    Args:
        request: request
        image_id: ID изображения

    Returns: url image_page

    """
    if request.method == 'POST':
        form = ChangeSizeForm(request.POST)

        if form.is_valid():
            height = int(form.data['height'])
            width = int(form.data['width'])

            # объект изображения
            image_obj = Image.objects.get(pk=image_id)
            # путь до изображения
            image_path = image_obj.original_image.path
            image_path_for_save = image_obj.image.path

            # изменяем размер с помощью Pillow
            img = ImagePIL.open(image_path)
            img = img.resize((width, height), ImagePIL.ANTIALIAS)

            # сохранение изображения
            try:
                img.save(image_path_for_save, format='JPEG')

            except:
                rgb_im = img.convert('RGB')
                rgb_im.save(image_path_for_save, format='JPEG')
                rgb_im.close()
            img.close()

            return redirect('image_page', image_obj.id)

    else:
        # возвращаем форму и объект изображения
        form = ChangeSizeForm()
        image_obj = Image.objects.get(pk=image_id)
        return render(request, 'app/image-page.html', {'form': form, 'image_obj': image_obj})


def add_image_view(request):
    """
    Представление для добавления изображения
    Args:
        request: request

    Returns: redirect - url image_page or render - url add_image

    """
    if request.method == 'POST':
        form = AddImageForm(request.POST or None, request.FILES or None)

        # Если форма валидна сохраняем изображение
        if form.is_valid():
            image_data = form.cleaned_data['image'] or None
            image_url = form.cleaned_data['link'] or None

            # Если пришла дата с файлом изображения
            if image_data:
                title = image_data.name
                image = request.FILES['image']
                original_image = request.FILES['image']
                image = Image.objects.create(title=title, image=image,
                                             original_image=original_image)
                image.save()

                return redirect('image_page', image.id)

            # Если пришла дата ссылкой
            if image_url:
                resp = requests.get(image_url)

                # Запрос был в порядке?
                if resp.status_code != requests.codes.ok:
                    # Нет, обработка ошибок, пропуск файла и т. Д. И т. Д.
                    form = AddImageForm()
                    return render(request, 'app/add-image.html', {'form': form})

                # Получите имя файла из URL-адреса, которое будет использоваться для сохранения позже
                srez = len(image_url) - 4
                file_name = image_url[srez:]

                # запись в буфер памяти временное изображение
                fp = BytesIO()
                fp.write(resp.content)

                # Создайте модель, в которую хотите сохранить изображение.
                image = Image()

                # Сохраните временное изображение в модель
                # Это сохраняет модель, поэтому убедитесь, что она действительна.
                image.image.save(file_name, files.File(fp))
                image.original_image.save(file_name, files.File(fp))
                image.title = file_name + '-id' + str(image.id)
                image.save()

                return redirect('image_page', image.id)

    else:
        form = AddImageForm()
        return render(request, 'app/add-image.html', {'form': form})

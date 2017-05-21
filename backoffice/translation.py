from modeltranslation.translator import translator, TranslationOptions
from backoffice.models import ProductType,ProductBrand,ProductSubType,ProductReferences,Product


class ProductTypeTranslationOptions(TranslationOptions):
    fields=("Type",)

#translator.register(ProductType,ProductTypeTranslationOptions)


class ProductSubTypeTranslationOptions(TranslationOptions):
    fields=("SubType",)

#translator.register(ProductSubType,ProductSubTypeTranslationOptions)

class ProductReferencesTranslationOptions(TranslationOptions):
    fields=("Ref",)

#translator.register(ProductReferences,ProductReferencesTranslationOptions)

class ProductTranslationOptions(TranslationOptions):
    fields=("ProductName","Description")
    fallback_values = 'à traduire !'

#translator.register(Product,ProductTranslationOptions)
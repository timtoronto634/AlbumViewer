import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.images import Images

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.IMAGES: Images,
    }
)

path_to_api = PathToApi(
    {
        PathValues.IMAGES: Images,
    }
)

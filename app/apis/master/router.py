""" Master APIs router """
from fastapi import APIRouter
from app.connections import database

router = APIRouter(
    prefix="/api/master"
)

@router.get("/database/refresh_db")
def refresh_db():
    """ Reset models and seeders """
    database.refresh_db()
    return "DB refreshed"

# pylint: disable=self-assigning-variable
# pylint: disable=unspecified-encoding
# pylint: disable=f-string-without-interpolation
# pylint: disable=consider-using-with
# pylint: disable=import-outside-toplevel
# pylint: disable=bare-except
# pylint: disable=too-many-statements
@router.get("/create_api")
def create_api(
        module_name: str,
        api_name: str
    ):
    """ Create API """
    import os
    def use_dir(route):
        try:
            os.stat(route)
        except:
            os.mkdir(route)
    def convert_to_camel_case(value):
        strings = value.split('_')
        return ''.join(word.capitalize() for word in strings)
    module_name = module_name
    api_name = api_name
    dir_name_module = f"app/apis/{module_name}/"
    use_dir(dir_name_module)
    dir_name_api = f'{dir_name_module}/{api_name}'
    use_dir(dir_name_api)
    class_name = convert_to_camel_case(api_name)

    # Create input.py
    file = open(dir_name_api + "/input.py", "w")
    file.write(f'""" Defines the input schema of the API {class_name} """\n')
    file.write(f'from pydantic import BaseModel\n\n')
    file.write(f'class {class_name}Body(BaseModel):\n')
    file.write(f'    """ Body API """\n\n')
    file.write(f'class {class_name}Query(BaseModel):\n')
    file.write(f'    """ Query API """\n\n')
    file.write(f'class {class_name}Header(BaseModel):\n')
    file.write(f'    """ Header API """\n\n')
    file.write(f'class {class_name}Path(BaseModel):\n')
    file.write(f'    """ Path API """\n\n')
    file.write(f'class {class_name}Input(\n')
    file.write(f'    {class_name}Body,\n')
    file.write(f'    {class_name}Query,\n')
    file.write(f'    {class_name}Header,\n')
    file.write(f'    {class_name}Path\n')
    file.write(f'):\n')
    file.write(f'    """ Input API """\n')
    file.close()

    # Create output.py
    file = open(dir_name_api + "/output.py", "w")
    file.write(f'""" Defines the output schema of the API {class_name} """\n')
    file.write(f'from pydantic import BaseModel\n\n')
    file.write(f'class {class_name}Output(BaseModel):\n')
    file.write(f'    """ Output API """\n')
    file.close()

    # Create flow.py
    file = open(dir_name_api + "/flow.py", "w")
    file.write(f'""" Defines the flow of the API {class_name} """\n')
    file.write(f'from libraries.api_manager.flow.flow_api import FlowAPI\n')
    file.write(f'from .input import {class_name}Input\n\n')
    file.write(f'class {class_name}Flow(FlowAPI):\n')
    file.write(f'    """ Class that defines the API flow """\n\n')
    file.write(f'    def __init__(self):\n')
    file.write(f'        super().__init__()\n')
    file.write(f'        self.request:{class_name}Input\n\n')
    file.write(f'    def execute(self):\n')
    file.write(f'        """ Function that ejecutes the flow """\n')
    file.write(f'        return dict()\n')
    file.close()

    # Create response.py
    file = open(dir_name_api + "/response.py", "w")
    file.write(f'""" Defines the response of the API {class_name} """\n')
    file.write(f'from libraries.api_manager.response.response_api import ResponseAPI\n')
    file.write(f'from libraries.api_manager.response.model_fields import ModelFields\n\n')
    file.write(f'class {class_name}Response(ResponseAPI):\n')
    file.write(f'    """ Class that defines the API response"""\n\n')
    file.write(f'    def set_response(self):\n')
    file.write(f'        """ Function that sets the response structure """\n')
    file.write(f'        self.set_structure([\n')
    file.write(f'            ModelFields()\n')
    file.write(f'        ])\n\n')
    file.close()

    # Create validator.py
    file = open(dir_name_api + "/validator.py", "w")
    file.write(f'""" Defines the validations of the API {class_name} """\n')
    file.write(f'from libraries.api_manager.validator.validator_api import ValidatorAPI\n')
    file.write(f'from .input import {class_name}Input\n\n')
    file.write(f'class {class_name}Validator(ValidatorAPI):\n')
    file.write(f'    """ Class that validates the input of the API """\n\n')
    file.write(f'    def __init__(self):\n')
    file.write(f'        super().__init__()\n')
    file.write(f'        self.request:{class_name}Input\n\n')
    file.write(f'    def validate_api(self):\n')
    file.write(f'        """ Function that ejecutes all the validations """\n')
    file.close()

    # Create module.py
    file = open(dir_name_api + "/module.py", "w")
    file.write(f'""" Defines the module of the API {class_name} """\n')
    file.write(f'from libraries.api_manager.module.module_api import ModuleAPI\n')
    file.write(f'from .response import {class_name}Response\n')
    file.write(f'from .flow import {class_name}Flow\n')
    file.write(f'from .validator import {class_name}Validator\n\n')
    file.write(f'class {class_name}Module(ModuleAPI):\n')
    file.write(f'    """ Class that controls the components of the API """\n\n')
    file.write(f'    def __init__(self, request, db):\n')
    file.write(f'        super().__init__()\n')
    file.write(f'        self.request = request\n')
    file.write(f'        self.validator_api = {class_name}Validator()\n')
    file.write(f'        self.flow_api = {class_name}Flow()\n')
    file.write(f'        self.response_api = {class_name}Response()\n')
    file.write(f'        self.is_searchable = False\n')
    file.write(f'        self.db = db\n')
    file.close()

    # Create router.py
    file = open(dir_name_api + "/router.py", "w")
    file.write(f'""" Defines the router funtion of the API {class_name} """\n')
    file.write(f'from fastapi import APIRouter, Depends, Body\n')
    file.write(f'from requests import Session\n')
    file.write(f'from app.connections.database import get_db\n')
    file.write(f'from libraries.utils.auth_bearer import JWTBearer\n')
    file.write(f'from .module import {class_name}Module\n')
    file.write(f'from .input import (\n')
    file.write(f'    {class_name}Body,\n')
    file.write(f'    {class_name}Header,\n')
    file.write(f'    {class_name}Path,\n')
    file.write(f'    {class_name}Query,\n')
    file.write(f'    {class_name}Input\n')
    file.write(f')\n')
    file.write(f'from .output import {class_name}Output\n\n')
    file.write(f'API_MODULE = "ModuleName"\n')
    file.write(f'router = APIRouter(tags=[API_MODULE], dependencies=[Depends(JWTBearer())])\n\n')
    file.write(f'@router.post("api/", response_model={class_name}Output)\n')
    file.write(f'def api_{api_name}(\n')
    file.write(f'    path: {class_name}Path = Depends(),\n')
    file.write(f'    header: {class_name}Header = Depends(),\n')
    file.write(f'    query: {class_name}Query = Depends(),\n')
    file.write(f'    body: {class_name}Body = Body(),\n')
    file.write(f'    db: Session = Depends(get_db)\n')
    file.write(f'    ):\n')
    file.write(f'    """ Instance and run the API module """\n\n')
    file.write(f'    module = {class_name}Module({class_name}Input.parse_obj(\u007B\n')
    file.write(f'        **path.dict(),\n')
    file.write(f'        **header.dict(),\n')
    file.write(f'        **query.dict(),\n')
    file.write(f'        **body.dict()\n')
    file.write(f'    \u007D), db)\n')
    file.write(f'    return module.use_api()\n')
    file.close()
    return "API Created"

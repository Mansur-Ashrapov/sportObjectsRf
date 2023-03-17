from databases import Database
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from app.container import ProjectContainer
from app.repositories import (
    CuratorRepo,
    SportObjectRepo
)
from app.schemas.sport_objects import (
    SportObjectOut,
    SportObjectPoint
)

router = APIRouter()


@router.get('/{lang}&{id}/', response_model=SportObjectOut)
@inject
async def get_one_by_id(
        id: int,
        lang: str,
        curator_repo: CuratorRepo = Depends(Provide[ProjectContainer.curator_repo]),
        sport_objects_repo: SportObjectRepo = Depends(Provide[ProjectContainer.sport_objects_repo])
    ):
    try:
        object = await sport_objects_repo.get_all_by_id(id, lang)
        curator = await curator_repo.get_by_id(object.curator_id, lang)
        
        if object == None:
            return {}
        
        if curator == None:
            return SportObjectOut(**object.dict())
        return SportObjectOut(**object.dict(), curator=curator)
    except Exception as e:
        print(e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    

@router.get('/points/{lang}/', response_model=list[SportObjectPoint])
@inject
async def get_all_points(
        lang: str,
        sport_objects_repo: SportObjectRepo = Depends(Provide[ProjectContainer.sport_objects_repo])
    ):
    try:
        points = await sport_objects_repo.get_all_point_objects(lang)

        if points == None:
            return {}    
        return points
    except Exception as e:
        print(e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    

@router.get('/finance/')
@inject
async def get_finance(
        sport_objects_repo: SportObjectRepo = Depends(Provide[ProjectContainer.sport_objects_repo])
    ):
    try:
        financies = await sport_objects_repo.get_full_finance_by_regions()

        if financies == None:
            return {}
        
        regions_by_summ = {}
        for key, value in financies.items():
            items = value.values()
            regions_by_summ[key] = sum(items)
        regions_by_summ = [{'name': k, 'uv': v, 'pv': 2400, 'amt': 2400} for k, v in regions_by_summ.items()]

        return [regions_by_summ, financies]
    except Exception as e:
        print(e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR
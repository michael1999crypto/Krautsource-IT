using KrautSourceWebApi.DTOS;
using KrautSourceWebApi.Models;

namespace KrautSourceWebApi.Profiles
{
    public class DatasProfile : AutoMapper.Profile
    {
        public DatasProfile()
        {
            CreateMap<CreateDataDto, Data>();
            CreateMap<Data, DataDto>();
        }
    }
}

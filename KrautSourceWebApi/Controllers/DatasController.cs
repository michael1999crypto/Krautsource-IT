using AutoMapper;
using KrautSourceWebApi.DTOS;
using KrautSourceWebApi.Models;
using Microsoft.AspNetCore.Mvc;

namespace KrautSourceWebApi.Controllers
{
    [ApiController]
    [Route("api/datas")]
    public class DatasController : ControllerBase
    {
        private readonly IKrautSourceRepository krautSourceRepository;
        private readonly IMapper mapper;

        public DatasController(IKrautSourceRepository _krautSourceRepository, IMapper _mapper)
        {
            krautSourceRepository = _krautSourceRepository;
            mapper = _mapper;
        }

        [HttpPost]
        public ActionResult PostData(CreateDataDto data)
        {
            Data dataEntity = mapper.Map<Data>(data);
            krautSourceRepository.CreateData(dataEntity);

            var dataToReturn = mapper.Map<DataDto>(dataEntity);
            return Created("GET action in developement", dataToReturn);
        }
    }
}

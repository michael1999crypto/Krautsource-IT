using KrautSourceWebApi.Models;
using System;
using System.ComponentModel.DataAnnotations;

namespace KrautSourceWebApi.DTOS
{
    public class CreateDataDto
    {
        [Required]
        public string Id { get; set; }

        public string ConsumerType { get; set; }

        [Required]
        public string TypeOfData { get; set; }

        [Required]
        public string Value { get; set; }

        public LocationDto Position { get; set; }
    }
}

using KrautSourceWebApi.Models;
using System;
using System.ComponentModel.DataAnnotations;

namespace KrautSourceWebApi.DTOS
{
    public class CreateDataDto
    {
        [Required]
        public string TypeOfData { get; set; }

        [Required]
        public string Value { get; set; }

        public Location Position { get; set; }
    }
}

using System.ComponentModel.DataAnnotations;

namespace KrautSourceWebApi.Models
{
    public class Location
    {
        [Key]
        public string idLocation { get; set; }
        public double Longitude { get; set; }
        public double Latitude { get; set; }
    }
}

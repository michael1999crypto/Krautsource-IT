using Microsoft.EntityFrameworkCore;

namespace KrautSourceWebApi.Models
{
    public class KrautDbContext : DbContext
    {
        public KrautDbContext(DbContextOptions<KrautDbContext> options) : base(options)
        {

        }

        public DbSet<Data> Data { get; set; }
    }
}

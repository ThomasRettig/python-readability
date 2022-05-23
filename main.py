import textstat
from rich.console import Console

console = Console()

test_data = (
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ullamcorper suscipit placerat. Proin gravida purus non posuere maximus. Proin iaculis sapien justo, sed sagittis quam tempus ut. Nullam vehicula felis mauris, sed bibendum leo fermentum id. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vitae vulputate lacus, ac facilisis justo. Cras nulla tellus, viverra at velit sed, rutrum molestie purus. In mollis justo quam, nec hendrerit eros pulvinar eu. Fusce fringilla lorem id augue tristique dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut nulla velit, convallis at viverra dignissim, rhoncus vel dui.

    Nunc hendrerit at turpis et mattis. Pellentesque nec venenatis quam, eu suscipit risus. Nam sed dignissim sapien, vel maximus lorem. Aliquam at tincidunt neque. Integer ut sapien tellus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Phasellus sit amet cursus sem. Mauris a ultricies ipsum, id interdum lectus. Suspendisse pretium malesuada neque, nec scelerisque ligula cursus a. Fusce ut pulvinar mauris, vitae mattis nulla. Nulla vitae efficitur ante, in vulputate lacus. Mauris sed efficitur nulla. In condimentum mi non dui vulputate euismod. Sed posuere elit quis interdum venenatis.

    Proin sed purus ut felis ullamcorper pulvinar in vitae leo. Proin laoreet metus non ipsum auctor, sollicitudin pellentesque est maximus. Vivamus vitae ligula sit amet felis consequat ultrices. Sed eget ullamcorper arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam dapibus dui at turpis vehicula, nec interdum risus eleifend. Nam ac eros velit.

    In lobortis turpis felis, in suscipit eros sodales et. Sed tempor diam vitae porta lacinia. Mauris sit amet felis rutrum, pellentesque arcu at, volutpat magna. Duis vitae pellentesque nisl. Duis sodales placerat fermentum. Phasellus rutrum nunc elementum, scelerisque dui ac, aliquam elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Quisque ac nisi in ante volutpat dapibus id a neque. Nulla pharetra quis nisl in dignissim. Nunc vel lectus euismod, ultricies felis et, egestas ex. Pellentesque consectetur venenatis viverra. Maecenas eleifend, dui non consectetur aliquam, nisi tortor vulputate nisi, ac imperdiet felis nulla non dolor.

    Curabitur sit amet felis quis felis ultricies elementum sit amet vel nunc. In aliquam massa nec velit finibus, quis mattis orci rhoncus. Sed laoreet, sapien sed auctor pulvinar, erat risus condimentum dolor, eu pellentesque metus mauris non orci. Pellentesque pellentesque finibus tellus quis tincidunt. Nunc cursus elementum porta. Aenean iaculis dui erat, eu aliquet eros maximus a. Phasellus sodales tincidunt pellentesque. Curabitur vel quam mauris. Donec iaculis est at mauris accumsan, sit amet malesuada lectus vehicula. Quisque et sem a risus mattis tristique. Vivamus eget commodo felis. Sed sagittis pulvinar nulla, sit amet finibus lorem euismod eu.
    """
)

console.print("[green bold]Flesch reading ease:[/green bold]", textstat.flesch_reading_ease(test_data))
console.print("[green bold]Flesch-Kincaid:[/green bold]", textstat.flesch_kincaid_grade(test_data))
console.print("[green bold]SMOG index:[/green bold]", textstat.smog_index(test_data))
console.print("[green bold]Coleman-Liau index:[/green bold]", textstat.coleman_liau_index(test_data))
console.print("[green bold]Automated readability:[/green bold]", textstat.automated_readability_index(test_data))
console.print("[green bold]Dale-Chall readability score:[/green bold]", textstat.dale_chall_readability_score(test_data))
console.print("[green bold]Difficult words:[/green bold]", textstat.difficult_words(test_data))
console.print("[green bold]Linsear write formula:[/green bold]", textstat.linsear_write_formula(test_data))
console.print("[green bold]Fog scale:[/green bold]", textstat.gunning_fog(test_data))
console.print("[green bold]Reading time:[/green bold]", textstat.reading_time(test_data, ms_per_char=14.69))
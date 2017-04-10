import datetime

top_schools = ["School A", "School B", "School C"]
selected_schools = 3

unf_message = """Hello {name}!

Thank you for the the time you sent developing and building programs
that can propel a worthy and dedicated student to the next steps on their
path.

On this date I desired to understand more about your University, it's culture
and impact on society. Post my research I learned many things that impact my
synopsis that your institution would be a great place for me to challenge myself
learn and grow.

Even ${total} can't value the exitement I have about taking the journey ahead
with fate's choice of school. A choice based on hardwork and mutual interest.

I hope you are just as excited to learn about my background, if not I understand.
For many days I've contemplated how to make an impact on the world and the
hearts and minds of whomever should follow my story or invest in my strategies.

Thank you for the time spent.

 - Michael Ballard
{date}
 """

def make_message(schools):
    messages = schools
    if selected_schools == 3:
        i = 0
        for school in schools:
            message = unf_message.format(
                    name = school,
                    date = datetime.datetime.now(),
                    total = 150.00
            )
            print(message)

make_message(top_schools)
